from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")



def scan_site(url):

    try:

        # Add https if missing
        if not url.startswith("http://") and not url.startswith("https://"):
            url = "https://" + url

        response = requests.get(
            url,
            timeout=10,
            allow_redirects=True,
            verify=True,
            headers={
                "User-Agent":
                "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
        )

        result = {
            "url": url,
            "status": response.status_code,
            "server": response.headers.get(
                "Server",
                "Not Found"
            ),
            "content_type": response.headers.get(
                "Content-Type",
                "Not Found"
            ),
            "hsts": response.headers.get(
                "Strict-Transport-Security",
                "Missing"
            ),
            "csp": response.headers.get(
                "Content-Security-Policy",
                "Missing"
            ),
            "xframe": response.headers.get(
                "X-Frame-Options",
                "Missing"
            )
        }

        return result

    except requests.exceptions.ConnectionError:

        return {
            "error":
            "Connection failed. Check internet connection."
        }

    except requests.exceptions.Timeout:

        return {
            "error":
            "Request timeout."
        }

    except requests.exceptions.SSLError:

        return {
            "error":
            "SSL Certificate Error."
        }

    except Exception as e:

        return {
            "error": str(e)
        }




@app.route("/scan", methods=["POST"])
def scan():

    try:

        url = request.form.get("url")

        if not url:

            return render_template(
                "result.html",
                result={
                    "error":
                    "Please enter a URL."
                }
            )

        result = scan_site(url)

        return render_template(
            "result.html",
            result=result
        )

    except Exception as e:

        return render_template(
            "result.html",
            result={
                "error": str(e)
            }
        )




if __name__ == "__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )