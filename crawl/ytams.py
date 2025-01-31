import os
import time
import signal
import psutil
import shutil
import getpass  # 🔹 비밀번호 입력 시 화면에 노출되지 않도록 함
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

# 🔹 Python 출력을 즉시 표시하도록 설정
import sys
sys.stdout.reconfigure(line_buffering=True)

# 🔹 사용자 입력 (ID & Password)
user_id = input("📝 Enter your ID: ")
user_pw = getpass.getpass("🔒 Enter your Password: ")  # 입력할 때 화면에 보이지 않음

# 🔹 ChromeDriver 실행
print("🔹 ChromeDriver 실행 중...", flush=True)
service = Service("C:/chromedriver-win64/chromedriver.exe")  # 백슬래시 `\` 오류 방지를 위해 `/` 사용
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# 🔹 Selenium 탐지 방지
driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source": "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
})

# 🔹 웹사이트 접속 (타임아웃 설정)
print("🔹 웹사이트 접속 중...", flush=True)
driver.set_page_load_timeout(10)
driver.get("http://ytams.yura.co.kr/")

# 🔹 페이지 로딩 대기
print("🔹 페이지 로딩 대기 중...", flush=True)
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))
print("✅ 페이지 로딩 완료!", flush=True)

# 🔹 iframe 확인 및 이동
iframes = driver.find_elements(By.TAG_NAME, "iframe")
print(f"🔹 감지된 iframe 개수: {len(iframes)}")

if iframes:
    driver.switch_to.frame(iframes[0])
    print("✅ iframe 내부로 이동 완료!")

# 🔹 로그인 입력 필드 찾기
print("🔹 로그인 입력 필드 찾는 중...")
try:
    id_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "mberId")))
    print("✅ ID 입력 필드 찾음!")
except:
    print("❌ ID 입력 필드 찾기 실패!")

try:
    pw_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "password")))
    print("✅ Password 입력 필드 찾음!")
except:
    print("❌ Password 입력 필드 찾기 실패!")

# 🔹 JavaScript로 ID 및 Password 입력 (send_keys() 차단 방지)
try:
    driver.execute_script("arguments[0].value = arguments[1];", id_input, user_id)
    driver.execute_script("arguments[0].value = arguments[1];", pw_input, user_pw)
    print("✅ ID와 비밀번호 입력 완료!")
except:
    print("❌ ID 및 비밀번호 입력 실패!")

# 🔹 로그인 버튼 클릭 (JavaScript 방식)
try:
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//*[@id="compose"]'))
    )
    driver.execute_script("arguments[0].click();", login_button)
    print("✅ 로그인 버튼 클릭 완료!")
except:
    print("❌ 로그인 버튼 클릭 실패!")

# 🔹 자동 종료 방지
input("브라우저를 닫으려면 엔터를 누르세요...")

driver.quit()
