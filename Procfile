web: gunicorn app_url:app

worker: gunicorn otp_send.py
worker: gunicorn otp_verify.py
worker: gunicorn send_sms.py
worker: gunicorn pdf.py
worker: gunicorn aws_sentiment_capture.py
