import requests

def get_weather():
    # URL برای دریافت اطلاعات هوا در اصفهان با استفاده از سایت wttr.in
    url = "https://wttr.in/Isfahan?format=%t+%C+%w+%h"

    try:
        # ارسال درخواست به سایت wttr.in و دریافت پاسخ
        response = requests.get(url)

        # تنظیم کدگذاری UTF-8 برای خروجی
        response.encoding = 'utf-8'

        # دریافت اطلاعات هوا
        weather_info = response.text
        
        return weather_info
    
    except Exception as e:
        return f"خطا در درخواست به سایت wttr.in: {str(e)}"

# فراخوانی تابع و دریافت اطلاعات هوا


