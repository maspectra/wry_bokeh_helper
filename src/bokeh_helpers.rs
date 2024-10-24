use std::time::Duration;
use tao::{
    event::{Event, StartCause, WindowEvent},
    event_loop::{ControlFlow, EventLoopBuilder, EventLoopProxy},
    platform::run_return::EventLoopExtRunReturn,
    window::WindowBuilder,
};
use tokio::sync::broadcast::Sender;
use tokio::time::timeout;
use wry::{http::Request, WebViewBuilder};

pub enum UserEvent {
    PayloadReceived(String),
}

pub struct BokehCDNResource {
    pub version: String,
}

pub struct BokehLocalResource {
    pub file_uri: String,
}

pub enum BokehResource {
    CDN(BokehCDNResource),
    Local(BokehLocalResource),
}

fn ipc_handler(payload: &Request<String>, event_loop_proxy: &EventLoopProxy<UserEvent>) {
    let _ = event_loop_proxy.send_event(UserEvent::PayloadReceived(payload.body().clone()));
}

fn bokeh_resource_as_script_html(resource: Option<BokehResource>) -> String {
    match resource {
        Some(BokehResource::CDN(BokehCDNResource { version })) => {
            format!(
                "<script type='text/javascript' src='https://cdn.bokeh.org/bokeh/release/bokeh-{}.min.js'></script>",
                version
            )
        }
        Some(BokehResource::Local(BokehLocalResource { file_uri })) => format!("<script type='text/javascript' src='file:///{}'></script>", file_uri),
        None => "<script type='text/javascript' src='https://cdn.bokeh.org/bokeh/release/bokeh-3.5.2.min.js'></script>".to_string(),
    }
}

fn build_bokeh_render_html(resource: Option<BokehResource>) -> String {
    format!(
        "
        <html>
            <head>
            <style>
                html, body {{
                    box-sizing: border-box;
                    display: flow-root;
                    height: 100%;
                    margin: 0;
                    padding: 0;
                }}
            </style>
            {}
            <script type='text/javascript'>
                function renderBokeh(json) {{
                    console.log('Rendering Bokeh plot in WebView, json:', json);
                    const data = JSON.parse(json);
                    const rootId = data['root_id'];
                    if (window.Bokeh === undefined) {{
                        throw new Error('Bokeh is not loaded');
                    }}
                    window.Bokeh.embed.embed_item(data, document.getElementById('root')).then((viewManager) => {{
                        const view = viewManager.get_by_id(rootId);
                        const dataURL = view.export().canvas.toDataURL('image/png', 1.0);
                        window.ipc.postMessage(dataURL);
                    }});
                }}
            </script>
            </head>
            <body>
            <div id='root'></div>
            </body>
        </html>
        ",
        bokeh_resource_as_script_html(resource)
    )
}

fn do_render_bokeh_in_webview(
    json_data: &str,
    sender: Sender<String>,
    resource: Option<BokehResource>,
) {
    let mut event_loop = EventLoopBuilder::<UserEvent>::with_user_event().build();
    let event_loop_proxy = event_loop.create_proxy();
    let window = WindowBuilder::new()
        .with_decorations(false)
        .with_visible(false)
        .with_transparent(true)
        .build(&event_loop)
        .unwrap();

    let webview = WebViewBuilder::new()
        .with_html(build_bokeh_render_html(resource))
        .with_ipc_handler(move |payload| ipc_handler(&payload, &event_loop_proxy))
        .with_transparent(true)
        .build(&window)
        .unwrap();

    webview
        .evaluate_script(&format!(
            "window.onload = () => renderBokeh(`{}`)",
            json_data
        ))
        .unwrap();

    let _ = event_loop.run_return(move |event, _, control_flow| {
        *control_flow = ControlFlow::Wait;

        match event {
            Event::NewEvents(StartCause::Init) => {
                println!("Wry has started!")
            }
            Event::WindowEvent {
                event: WindowEvent::CloseRequested,
                ..
            } => *control_flow = ControlFlow::Exit,
            Event::UserEvent(UserEvent::PayloadReceived(payload)) => {
                sender.send(payload).unwrap();
                *control_flow = ControlFlow::Exit;
            }
            _ => (),
        }
    });
}

pub async fn render_bokeh_in_webview(json_data: &str, resource: Option<BokehResource>) -> String {
    let (tx, mut rx) = tokio::sync::broadcast::channel(1);
    do_render_bokeh_in_webview(json_data, tx, resource);

    rx.recv().await.unwrap()

    // let timeout_duration = Duration::from_secs(5);

    // match timeout(timeout_duration, rx.recv()).await {
    //     Ok(message) => {
    //         println!("333");
    //         message.unwrap()
    //     }
    //     Err(_) => {
    //         println!("111");
    //         panic!("Timeout after {:?}", timeout_duration);
    //     }
    //     _ => {
    //         println!("222");
    //         panic!("Timeout after {:?}", timeout_duration);
    //     }
    // }
}
