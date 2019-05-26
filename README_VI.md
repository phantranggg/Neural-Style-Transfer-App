# Ứng dụng chuyển đổi style ảnh - Neural Style Transfer

Ứng dụng web chuyển đổi style ảnh sử dụng công nghệ học máy.

Để sử dụng ứng dụng, bạn cần chuẩn bị 2 ảnh, ảnh thứ nhất là ảnh chứa nội dung, ảnh thứ 2 là ảnh chứa style muốn chuyển đổi.

Có thể sẽ mất 1 vài phút tùy vào cấu hình máy để tạo ảnh mới từ 2 ảnh đầu vào.

## Yêu cầu

- [virtualenv](https://virtualenv.pypa.io/en/latest/)

- Python 3

- pip

## Cài đặt

Khởi chạy môi trường: 

```bash
virtualenv venv
source venv/bin/activate
```

Cài đặt các thư viện:

```bash
pip install -r requirements.txt
```

Bạn có thể xem danh sách các thư viện cần thiết bằng lệnh: 

```bash
pip list
```

Tải file model tại:

https://drive.google.com/file/d/1XQ2pTh7heTevGnUNkgeq5PxEGFfD1wPr/view?usp=sharing

sau đó copy vào thư mục `src/pretrained-model/`

## Khởi chạy ứng dụng

```bash
python3 src/upload.py
```
Lệnh này sẽ khởi chạy ứng dụng tại http://localhost:8001 . Sử dụng bất kỳ trình duyệt nào để truy cập và bắt đầu sử dụng ứng dụng.

## Tắt môi trường ảo

Chạy lệnh:

```bash
deactivate
```