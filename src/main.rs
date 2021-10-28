//use hyper::body::HttpBody as _;
use hyper::Client;
use hyper_tls::HttpsConnector;
use tokio::io::{stdout, AsyncWriteExt as _};

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error + Send + Sync>> {
    let _git_token: String = String::from("eTzvSgg8sFPRkzDhcXoo");

    let https = HttpsConnector::new();
    let client = Client::builder().build::<_, hyper::Body>(https);
    let uri = "https://3.121.74.13/api/v4/users".parse()?;
    let resp = client.get(uri).await?;
    println!("Response: {}", resp.status());

    Ok(())
}

//use std::collections::HashMap;
//
//#[tokio::main]
//async fn main() -> Result<(), Box<dyn std::error::Error>> {
//    let resp = reqwest::get("https://httpbin.org/ip")
//        .await?
//        .json::<HashMap<String, String>>()
//        .await?;
//    println!("{:#?}", resp);
//    Ok(())
//}
