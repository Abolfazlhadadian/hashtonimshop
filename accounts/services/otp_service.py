# """
# سرویس ارسال پیامک (SMS Service)
# ================================
#
# چرا اینجوری نوشتیم؟
# --------------------
# از یه الگوی طراحی به اسم "Strategy Pattern" استفاده کردیم:
# - یه کلاس پایه (abstract) داریم: BaseSMSService
# - هر پنل پیامکی یه کلاس جدا میشه که از اون ارث‌بری میکنه
# - فعلاً ConsoleSMSService داریم که فقط print میکنه (برای تست)
# - وقتی پنل SMS رو گرفتی، فقط یه کلاس جدید اضافه میکنی
#
# مثال:
#     service = get_sms_service()
#     service.send_otp("09123456789", "12345")
# """
#
# import logging
# from abc import ABC, abstractmethod
#
# # Logger: به جای print، از logging استفاده میکنیم
# # چرا؟ چون:
# # ۱) میتونی سطح مهم بودن پیام رو مشخص کنی (debug, info, warning, error)
# # ۲) خروجی رو به فایل/کنسول/هرجا بفرستی
# # ۳) توی production خودکار پیام‌های debug رو فیلتر میکنه
# logger = logging.getLogger(__name__)
#
#
# class BaseSMSService(ABC):
#     """
#     کلاس پایه (Abstract) برای سرویس پیامک.
#
#     ABC یعنی Abstract Base Class:
#     - نمیشه مستقیم ازش object ساخت
#     - هر کلاسی که ازش ارث‌بری کنه باید متد send_otp رو حتماً پیاده‌سازی کنه
#     - اگه پیاده‌سازی نکنه، پایتون خطا میده
#     """
#
#     @abstractmethod
#     def send_otp(self, phone_number: str, code: str) -> bool:
#         """
#         ارسال کد OTP به شماره موبایل.
#
#         Args:
#             phone_number: شماره موبایل (مثلاً "09123456789")
#             code: کد OTP (مثلاً "12345")
#
#         Returns:
#             True اگه ارسال موفق بود، False اگه نبود
#         """
#         pass
#
#
# class ConsoleSMSService(BaseSMSService):
#     """
#     سرویس پیامک برای محیط توسعه (Development).
#     به جای ارسال واقعی SMS، کد رو توی کنسول (ترمینال) چاپ میکنه.
#
#     وقتی سرور جنگو روشنه و OTP درخواست بدی،
#     کد رو توی ترمینال میبینی.
#     """
#
#     def send_otp(self, phone_number: str, code: str) -> bool:
#         # توی کنسول نشون بده — هم log میزنیم هم print
#         message = (
#             f"\n"
#             f"{'=' * 50}\n"
#             f"📱 OTP Code Sent!\n"
#             f"{'=' * 50}\n"
#             f"📞 Phone: {phone_number}\n"
#             f"🔑 Code:  {code}\n"
#             f"{'=' * 50}\n"
#         )
#         print(message)
#         logger.info("OTP code sent to %s (console mode)", phone_number)
#         return True
#
#
# # ──────────────────────────────────────────────────────────────
# # بعداً وقتی پنل SMS رو گرفتی، یه کلاس مثل این اضافه کن:
# # ──────────────────────────────────────────────────────────────
# #
# # class KavenegarSMSService(BaseSMSService):
# #     """سرویس ارسال SMS از طریق کاوه‌نگار"""
# #
# #     def __init__(self):
# #         self.api_key = os.environ.get('KAVENEGAR_API_KEY')
# #
# #     def send_otp(self, phone_number: str, code: str) -> bool:
# #         import requests
# #         url = f"https://api.kavenegar.com/v1/{self.api_key}/verify/lookup.json"
# #         params = {
# #             'receptor': phone_number,
# #             'token': code,
# #             'template': 'your-template-name',
# #         }
# #         response = requests.get(url, params=params)
# #         return response.status_code == 200
#
#
# def get_sms_service() -> BaseSMSService:
#     """
#     Factory Function — تابع کارخانه
#
#     این تابع تصمیم میگیره کدوم سرویس SMS رو برگردونه.
#     فعلاً همیشه ConsoleSMSService برمیگردونه.
#
#     وقتی پنل SMS رو گرفتی، فقط اینجا رو عوض میکنی:
#         return KavenegarSMSService()
#
#     چرا Factory؟
#     چون بقیه کد فقط get_sms_service() رو صدا میزنه
#     و اصلاً براش مهم نیست پشتش کدوم سرویسه.
#     """
#     return ConsoleSMSService()
import secrets


def generate_otp():
    return ''.join(
        str(secrets.randbelow(10))
        for _ in range(6)
    )