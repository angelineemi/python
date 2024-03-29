--********************doc infooo*****************************************
--create TABLE doc_inform(doc_id number(4),name varchar2(15),specialization varchar2(15),phno number(10),available_time varchar2(4) CHECK(available_time in('mor','aftn','eve')));
--insert into doc_inform(doc_id,name,specialization,phno,available_time) values(100,"santhosh","general surgeon",9698104709,"mor");
--insert into doc_inform(doc_id,name,specialization,phno,available_time) values(107,"betsy","paediatrician",9798144707,"aftn");
--insert into doc_inform(doc_id,name,specialization,phno,available_time) values(108,"rebecca","dermatologist",9798108709,"eve");
--insert into doc_inform(doc_id,name,specialization,phno,available_time) values(109,"preethi","ENT specialist",5798104709,"mor");
--insert into doc_inform(doc_id,name,specialization,phno,available_time) values(110,"sneha","psychiatrist",9798304709,"aftn");
--insert into doc_inform(doc_id,name,specialization,phno,available_time) values(111,"preetham","opthalmologist",8798104709,"eve");
--select* from doc_inform;
-- ************consultationnnn*****************************************
--create table consultation_info(id number(3),health_issue varchar2(15), fees number(4), consult_date date);
--insert into consultation_info(id,health_issue,fees,consult_date) values(101,"allergy",500,date());
--insert into consultation_info(id,health_issue,fees,consult_date) values(102,"allergy",500,date());
--insert into consultation_info(id,health_issue,fees,consult_date) values(103,"fever",500,date());
--insert into consultation_info(id,health_issue,fees,consult_date) values(104,"headache",500,date());
--insert into consultation_info(id,health_issue,fees,consult_date) values(105,"ear pain",500,date());
--insert into consultation_info(id,health_issue,fees,consult_date) values(106,"rashes",500,date());
--SELECT* from consultation_info;
--******patient infooooo***********************************************
--create TABLE patient_info(id number(3),title varchar2(4),first_name varchar2(15),last_name varchar2(15),age number(10), gender varchar2(6));
--insert into patient_info(id,title,first_name,last_name,age,gender) values(101,"miss","ange","emi",20,"female");
--insert into patient_info(id,title,first_name,last_name,age,gender) values(102,"mr","chris","tomlin",30,"male");
--alter table patient_info add COLUMN email varchar2(15);
--update patient_info set email="ange.emimma@gmail.com" where id=101;
--update patient_info set email="chris123@gmail.com" where id=102;
--insert into patient_info(id,title,first_name,last_name,age,gender,email) values(103,"mrs","jeya","george",50,"female","jeya123@gmail.com");
--insert into patient_info(id,title,first_name,last_name,age,gender,email) values(104,"mr","jem","ashlin",30,"female","jemmyyy@gmail.com");
--insert into patient_info(id,title,first_name,last_name,age,gender,email) values(105,"mr","jason","punnuse",60,"male","jason123@gmail.com");
--insert into patient_info(id,title,first_name,last_name,age,gender,email) values(106,"mr","thomas","kuryan",70,"male","thommytom@gmail.com");
--select* FROM patient_info;
--retrieving specific columns
--select id,first_name,last_name from patient_info;
--alias
--SELECT id as patientid, first_name as firstname,last_name as lastname from patient_info;
--retieving with certain conditions
--select first_name, last_name from patient_info where gender="female";
--select first_name,last_name from patient_info where gender not like "female";
--select count(first_name) from patient_info where gender="male";
--SELECT p1.id,first_name,gender,consult_date from patient_info as p1 join consultation_info as c1 on p1.id=c1.id;
--SELECT*from doc_inform order by name;
--select first_name from patient_info GROUP by id;
