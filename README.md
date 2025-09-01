# GitHub Webhook Listener with Flask

This project is a simple **Flask-based webhook listener** for GitHub.  
It verifies incoming webhook requests using a secret key and processes specific events (e.g., issue creation).

---

## 📌 Features
- Verify GitHub webhook signatures (`X-Hub-Signature-256`)
- Handle **GitHub issue events** (`opened`, etc.)
- Log issue details (`title`, `URL`)
- Extendable for other event types (e.g., `push`, `pull_request`)
- JSON response for success or error cases

---

## ⚙️ Requirements
- Python **3.8+**
- Flask

Install dependencies:

```bash
pip install flask
```

---

## 🚀 Usage

1. **Clone this repository**  
   ```bash
   git clone https://github.com/yourusername/github-webhook-listener.git
   cd github-webhook-listener
   ```

2. **Set your GitHub webhook secret**  
   Edit the `WEBHOOK_SECRET` in the code:

   ```python
   WEBHOOK_SECRET = b"your-secret-key"
   ```

   ⚠️ Note: The secret must be in **bytes** (prefix with `b`).

3. **Run the Flask server**  
   ```bash
   python app.py
   ```

   The server will run on:  
   ```
   http://localhost:3006/webhook/github
   ```

4. **Configure GitHub Webhook**  
   - Go to your GitHub repository → **Settings → Webhooks**
   - Add a new webhook:
     - **Payload URL**: `http://your-server:3006/webhook/github`
     - **Content type**: `application/json`
     - **Secret**: same as `WEBHOOK_SECRET`
     - Choose events (e.g., *Issues*)

---

## 🔒 Security
- Uses **HMAC-SHA256** to validate signatures.
- Rejects requests with invalid or missing signatures.
- Ensures only **trusted GitHub events** are processed.

---

## 🛠️ Example: Issue Event
When a new issue is opened, the server logs:

```
🎯 New Issue Created: Example bug
🔗 URL: https://github.com/user/repo/issues/1
```

You can replace the `print` statements with:
- Sending notifications (Slack, Discord, Email, etc.)
- Writing to a database
- Triggering CI/CD pipelines

---

## 📂 Project Structure
```
.
├── app.py         # Main Flask application
├── README.md      # Project documentation
```

---

## 📌 Notes
- Make sure the server is **publicly accessible** if GitHub needs to reach it (use tools like [ngrok](https://ngrok.com/) for local testing).
- Always keep your `WEBHOOK_SECRET` safe and private.

---

## 📜 License
This project is open-source and available under the **MIT License**.
