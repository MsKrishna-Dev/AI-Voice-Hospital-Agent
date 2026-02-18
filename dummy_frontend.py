# step 5: Streamlit dashboard testing (Just for testing, my ai agent don't need an UI) 
import streamlit as st
import datetime as dt
import requests

st.title("AIIMS Hospital Appointment Booking Portal")
base_url = st.text_input("Backend URL", "http://127.0.0.1:4444").rstrip("/")

patient_name = st.text_input("Patient Name")
reason = st.text_input("Reason for Appointment")
start_date = st.date_input("Appointment Date", dt.date.today() + dt.timedelta(days=1))
start_time = st.time_input("Appointment Time", dt.time(9,0))

if st.button("Schedule"):
        start_dt = dt.datetime.combine(start_date, start_time)
        payload = {
          "patient_name": patient_name.strip(),
          "reason": reason.strip() or None,
          "start_date": start_dt.isoformat()
        }      
        try:
            resp = requests.post(f"{base_url}/schedule_appointments/", json=payload, timeout=10)
            resp.raise_for_status()
            st.success("Successfully scheduled appointment!")

        except requests.RequestException as exc:
            st.error(f"Failed to schedule appointment: {exc}")

st.divider()
st.subheader("Cancel Appointments")

cancel_patient_name = st.text_input("Patient Name to Cancel", key = "cancel_patient_name")
cancel_date = st.date_input("Date of cancel", key = "cancel_date", value=dt.date.today())

if st.button("Cancel Appointments"):
        payload = {
            "patient_name": cancel_patient_name.strip(),
            "date": cancel_date.isoformat()
        }
        try:
            resp = requests.post(f"{base_url}/cancel_appointments/", json=payload, timeout=10)
            resp.raise_for_status()
            # cancel_count = resp.json().get("cancel_count", 0)
            data = resp.json() if resp.content else {}
            # st.success(f"Canceled: {data.get('cancel_count', 0)}")
            cancel_count = data.get("cancel_count", 0)
            if data.get('cancel_count', 0) > 0:
             st.success(f"Successfully cancelled {data.get('cancel_count', 0)} appointment.")
            else:
             st.warning("No appointments found to cancel.")


        except requests.HTTPError as exc:
            st.error(f"Failed to cancel appointments: {exc}")   


st.divider()
st.subheader("Check Appointments")

appointment_date = st.date_input("Date to check appointments", key="check_appointment_date", value=dt.date.today())
if st.button("Check Appointments"):
        try:
            params = {"date": appointment_date.isoformat()}
            resp = requests.get(f"{base_url}/list_appointments/", params=params, timeout=10)
            resp.raise_for_status()
            st.dataframe(resp.json(), use_container_width=True, hide_index=True)
        except requests.RequestException as exc:
            st.error(f"Cannot load Appointments: {exc}")






