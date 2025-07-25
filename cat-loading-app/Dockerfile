FROM python:3.10-slim

# Cài đặt thư mục làm việc
WORKDIR /app

# Copy toàn bộ project vào container
COPY . .

# Cài đặt các package
RUN pip install --no-cache-dir -r requirements.txt

# Expose đúng cổng Cloud Run yêu cầu
EXPOSE 8080

# Thiết lập biến PORT mặc định để tránh lỗi
ENV PORT 8080

# Dùng shell để giải biến PORT
CMD streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
