CREATE TABLE IF NOT EXISTS cal_win_db.Users(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
name varchar(255),
last_name varchar(255),
username varchar(255),
passwd varchar(255),
birth varchar(255),
email varchar(255),
type varchar(255),
pic varbinary(5000),
status varchar(255),
gender varchar(255)
);

CREATE TABLE IF NOT EXISTS cal_win_db.Activity(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
status varchar(255),
submit_date DATETIME,
type varchar(255),
user_id varchar(60),
FOREIGN KEY (user_id) REFERENCES cal_win_db.Users(id)
);


CREATE TABLE IF NOT EXISTS cal_win_db.Question(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
content varchar(255),
u_id varchar(60),
FOREIGN KEY(u_id) REFERENCES cal_win_db.Users(id)
);

CREATE TABLE IF NOT EXISTS cal_win_db.Answer(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
content varchar(255),
u_id varchar(60),
quest_id varchar(60),
FOREIGN KEY(u_id) REFERENCES cal_win_db.Users(id),
FOREIGN KEY(quest_id) REFERENCES cal_win_db.Question(id)
);


CREATE TABLE IF NOT EXISTS cal_win_db.Calendar(
id varchar(60) PRIMARY KEY,
created_at DATETIME,
updated_at DATETIME,
c_date DATETIME,
text varchar(255),
user_id varchar(60),
quest_id varchar(60),
ans_id varchar(60),
act_id varchar(60),
FOREIGN KEY (user_id) REFERENCES cal_win_db.Users(id),
FOREIGN KEY (quest_id) REFERENCES cal_win_db.Question(id),
FOREIGN KEY (ans_id) REFERENCES cal_win_db.Answer(id),
FOREIGN KEY (act_id) REFERENCES cal_win_db.Activity(id)
);
