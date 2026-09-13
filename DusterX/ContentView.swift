import SwiftUI
import WebKit

struct ContentView: View {
    var body: some View {
        DusterWebView(url: URL(string: "https://lucasaasn-svg.github.io/duster-x/")!)
            .ignoresSafeArea()
    }
}

struct DusterWebView: UIViewRepresentable {
    let url: URL

    func makeUIView(context: Context) -> WKWebView {
        let config = WKWebViewConfiguration()
        config.allowsInlineMediaPlayback = true
        let webView = WKWebView(frame: .zero, configuration: config)
        webView.load(URLRequest(url: url))
        return webView
    }

    func updateUIView(_ webView: WKWebView, context: Context) {}
}
