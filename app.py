import os
import requests
import streamlit as st

st.set_page_config(page_title="Praveen Trading Alerts", page_icon="📈")
st.title("📈 Praveen Trading Alerts")
st.caption("Telegram notification test")

token = st.secrets.get("TELEGRAM_BOT_TOKEN", os.getenv("TELEGRAM_BOT_TOKEN", ""))
chat_id = st.secrets.get("TELEGRAM_CHAT_ID", os.getenv("TELEGRAM_CHAT_ID", ""))

if token and chat_id:
    st.success("Telegram details are configured.")
else:
    st.warning("Telegram secrets are not configured yet.")

if st.button("🔔 Send Test Notification", use_container_width=True):
    if not token or not chat_id:
        st.error("Add TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID in Streamlit Secrets first.")
    else:
        message = (
            "🟢 TEST NOTIFICATION\n\n"
            "Your trading alert system is connected successfully.\n\n"
            "Portfolio monitoring:\n"
            "• TMCV — 43 shares @ ₹460.77\n"
            "• Tata Gold ETF — 1,000 units @ ₹14.76\n\n"
            "This is only a test."
        )
        try:
            r = requests.post(
                f"https://api.telegram.org/bot{token}/sendMessage",
                data={"chat_id": chat_id, "text": message},
                timeout=15,
            )
            data = r.json()
            if r.ok and data.get("ok"):
                st.success("✅ Test notification sent. Check Telegram.")
            else:
                st.error(data.get("description", "Telegram rejected the message."))
        except Exception as e:
            st.error(f"Connection error: {e}")

st.divider()
st.write("After this test works, we can connect the same channel to SELL/STOP-LOSS and growth-stock alerts.")
