doc info
--create TABLE doc_info(doc_id number(4),name varchar2(15),specialization varchar2(15),phno number(10),available_time varchar2(4) CHECK(available_time in('mor','aftn','eve')));
--insert into doc_info (doc_id,name,specialization,phno,available_time) values(100,"santhosh","general surgeon",9798104709,"mor");
--select* from doc_info;
--value wont be changed because it violates the given constraint
--update doc_info set available_time="4" where name="santhosh";

patient info

--create TABLE patient_info(id number(3),title varchar2(4),first_name varchar2(15),last_name varchar2(15),age number(10), gender varchar2(6));
--insert into patient_info(id,title,first_name,last_name,age,gender) values(101,"miss","ange","emi",20,"female");
--insert into patient_info(id,title,first_name,last_name,age,gender) values(102,"mr","chris","tomlin",30,"male");
--alter table patient_info add COLUMN email varchar2(15);
--update patient_info set email="ange.emimma@gmail.com" where id=101;
--update patient_info set email="chris123@gmail.com" where id=102;
SELECT* from patient_info;

--create table consultation_info(id number(3),health_issue varchar2(15), fees number(4), consult_date date);
--insert into consultation_info(id,health_issue,fees,consult_date) values(101,"allergy",500,date());
select* from consultation_info;
