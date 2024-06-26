insert into doctor(account,password,reg_time) values("zhangsan", "7c4a8d09ca3762af61e59520943dc26494f8941b", "2024-01-01");
insert into doctor(account,password,reg_time) values("lisi", "1f8ac10f23c5b5bc1167bda84b833e5c057a77d2", "2024-01-01");

insert into patients(Patient_Name,Sex,Birth_Date) values("patient1", "男", "2024-01-01");
insert into patients(Patient_Name,Sex,Birth_Date) values("patient2", "男", "2024-01-01");
insert into patients(Patient_Name,Sex,Birth_Date) values("patient3", "男", "2024-01-01");
insert into patients(Patient_Name,Sex,Birth_Date) values("patient4", "男", "2024-01-01");

insert into doctorpatient(Doctor_ID,Patient_ID) values(1, 1);
insert into doctorpatient(Doctor_ID,Patient_ID) values(1, 2);
insert into doctorpatient(Doctor_ID,Patient_ID) values(1, 3);
insert into doctorpatient(Doctor_ID,Patient_ID) values(1, 4);

insert into images(Examine_Date,Image_Modality,Patient_ID,Diagnosis_Notes,Image_Data,Device,Number_of_images) values("2024-01-01 11:22:33", "CT", 1, "some desc", "data series", "CT", 100);
insert into images(Examine_Date,Image_Modality,Patient_ID,Diagnosis_Notes,Image_Data,Device,Number_of_images) values("2024-01-01 11:22:33", "CT", 1, "some desc", "data series", "CT", 100);
insert into images(Examine_Date,Image_Modality,Patient_ID,Diagnosis_Notes,Image_Data,Device,Number_of_images) values("2024-01-01 11:22:33", "CT", 1, "some desc", "data series", "CT", 100);
insert into images(Examine_Date,Image_Modality,Patient_ID,Diagnosis_Notes,Image_Data,Device,Number_of_images) values("2024-01-01 11:22:33", "CT", 2, "some desc", "data series", "MRI", 100);
insert into images(Examine_Date,Image_Modality,Patient_ID,Diagnosis_Notes,Image_Data,Device,Number_of_images) values("2024-01-01 11:22:33", "CT", 2, "some desc", "data series", "MRI", 100);
insert into images(Examine_Date,Image_Modality,Patient_ID,Diagnosis_Notes,Image_Data,Device,Number_of_images) values("2024-01-01 11:22:33", "CT", 2, "some desc", "data series", "MRI", 100);