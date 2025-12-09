from flask import Flask, render_template_string
import os

app = Flask(__name__)

# HTML template for the homepage
HTML_TEMPLATE = '''



    Panda App - Interview Prep

        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 50px auto;
            padding: 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
        }
        .container {
            background: rgba(255, 255, 255, 0.1);
            padding: 30px;
            border-radius: 10px;
            backdrop-filter: blur(10px);
        }
        h1 {
            text-align: center;
            margin-bottom: 30px;
        }
        .code-section {
            background: rgba(0, 0, 0, 0.3);
            padding: 20px;
            border-radius: 5px;
            margin: 20px 0;
        }
        code {
            color: #ffd700;
        }
        .footer {
            text-align: center;
            margin-top: 30px;
            opacity: 0.8;
        }




        🐼 Panda Interview Prep App


            Welcome!
            This app is deployed on Google Cloud Run using Cloud Build.
            Repository: rvvikash/panda
            Status: ✅ Running on GCP Free Tier



            📝 Sample Interview Questions
            Find second maximum salary from department
            Check out the Python examples in this repository!



            Deployed automatically on push to main branch 🚀




'''


@app.route('/')
def home():
    return render_template_string(HTML_TEMPLATE)


@app.route('/health')
def health():
    return {'status': 'healthy', 'service': 'panda-app'}, 200


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port, debug=False)