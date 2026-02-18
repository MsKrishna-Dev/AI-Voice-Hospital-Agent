# imports

# step 1: Import database objects

from urllib import request
from database import init_db, Appointment, get_db

init_db()

# step 3: Create data contracts (schemas) for request and response models using Pydantic
import datetime as dt
from pydantic import BaseModel
class AppointmentRequest(BaseModel):
    patient_name: str
    reason: str
    start_date: dt.datetime

class AppointmentResponse(BaseModel):
    id : int
    patient_name : str
    reason : str | None
    start_date : dt.datetime
    cancelled : bool
    created_at : dt.datetime


class CancelAppointmentRequest(BaseModel):
    patient_name: str
    date: dt.date

class CancelAppointmentResponse(BaseModel):
    cancel_count : int

class ListAppointmentRequest(BaseModel):
    date: dt.date

# step 2: Create FastAPI application & end-points (snippet codes which will tell what to do like get, put, push, delete, etc)

from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session

app = FastAPI()

# Schedule an appointment
@app.post("/schedule_appointments/")
def schedule_appointment(request: AppointmentRequest, db: Session = Depends(get_db)):
   
    new_appointment = Appointment(
        patient_name=request.patient_name,  
        reason=request.reason,
        start_date=request.start_date
    )

    db.add(new_appointment)
    db.commit() 
    db.refresh(new_appointment)
    new_appointment_return_obj = AppointmentResponse(
        id=new_appointment.id,
        patient_name=new_appointment.patient_name,
        reason=new_appointment.reason,
        start_date=new_appointment.start_date,
        cancelled=new_appointment.cancelled,
        created_at=new_appointment.created_at
    )
   
    return new_appointment_return_obj
     # logic for scheduling an appointment, write a row in db
    return

# Cancel an appointment
from sqlalchemy import select
@app.post("/cancel_appointments/")
def cancel_appointment(request: CancelAppointmentRequest, db: Session = Depends(get_db)):

    print("---- CANCEL REQUEST RECEIVED ----")
    print("Patient Name:", request.patient_name)
    print("Date:", request.date)

  # Show all appointments in DB
    all_appointments = db.query(Appointment).all()
    print("---- ALL APPOINTMENTS IN DB ----")
    for a in all_appointments:
        print(a.patient_name, a.start_date, a.cancelled)

    start_dt = dt.datetime.combine(request.date, dt.time.min)
    # end_dt = start_dt + dt.timedelta(days=1)
    end_dt = dt.datetime.combine(request.date, dt.time.max)

    # logic for scheduling an appointment, update/delete a row in db
    results = db.execute(
    select(Appointment)
    .where(Appointment.patient_name == request.patient_name)
    .where(Appointment.start_date >= start_dt)
    .where(Appointment.start_date < end_dt)
    .where(Appointment.cancelled == False)
    )

    appointments = results.scalars().all() 
    if not appointments:
        raise HTTPException(status_code=404, detail="No appointment found for the given patient and date")

    for appointment in appointments:
        appointment.cancelled = True

    db.commit()
    return CancelAppointmentResponse(cancel_count=len(appointments))

# List all appointments
@app.get("/list_appointments/")
def list_appointment(request: ListAppointmentRequest,db: Session = Depends(get_db)):
    # logic for scheduling an appointment, read a row from db
    start_dt = dt.datetime.combine(request.date, dt.time.min)
    end_dt = start_dt + dt.timedelta(days=1)


    results = db.execute(
        select(Appointment)
        .where(Appointment.cancelled == False)
        .where(Appointment.start_date >= start_dt)
        .where(Appointment.start_date < end_dt)
        .order_by(Appointment.start_date.asc())
        )
    return results.scalars().all()  

    book_appointment = []

    for appointment in results:
        appointment_obj = AppointmentResponse(
            appointment.id,
            appointment.patient_name,
            appointment.reason,
            appointment.start_date,
            appointment.cancelled,
            appointment.created_at
        )

        book_appointment.append(appointment_obj)

    return book_appointment


# step 4: Write actual code 

import uvicorn
if __name__ == "__main__": uvicorn.run("backend:app", host="127.0.0.1", port=4444, reload=True)

# step 5: Streamlit dashboard testing (Just for testing, my ai agent don't need an UI) (Check Dummy_frontend.py file )

