from flask import Flask, request, jsonify
import hmac
import hashlib
import json

app = Flask(__name__)

# کلید مخفی که در GitHub تنظیم کرده‌اید
WEBHOOK_SECRET = ""


def verify_signature(data, signature):
    """اعتبارسنجی امضای وب‌هوک"""
    computed_hash = hmac.new(WEBHOOK_SECRET, data, hashlib.sha256).hexdigest()
    expected_signature = 'sha256=' + computed_hash
    return hmac.compare_digest(expected_signature, signature)


@app.route('/webhook/github', methods=['POST'])
def handle_github_webhook():
    # دریافت هدرها و داده‌ها
    signature = request.headers.get('X-Hub-Signature-256')
    event_type = request.headers.get('X-GitHub-Event')
    print('1')
    if not signature or not event_type:
        return jsonify({'error': 'Missing headers'}), 400

    # اعتبارسنجی امضا
    if not verify_signature(request.data, signature):
        return jsonify({'error': 'Invalid signature'}), 403

    # پردازش انواع رویدادها
    if event_type == 'issues':
        payload = request.json
        action = payload.get('action')

        if action == 'opened':
            issue_title = payload['issue']['title']
            issue_url = payload['issue']['html_url']
            print(f'🎯 New Issue Created: {issue_title}')
            print(f'🔗 URL: {issue_url}')

            # اینجا می‌توانید عملیات مورد نظر را انجام دهید
            # مثلاً ارسال به Slack یا ذخیره در دیتابیس

    return jsonify({'status': 'success'}), 200


if __name__ == '__main__':
    app.run(port=3006, debug=True)