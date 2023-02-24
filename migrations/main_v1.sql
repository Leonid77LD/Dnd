CREATE TABLE Users (
	cduser uuid DEFAULT uuid_generate_v4(),
	nmuser VARCHAR NOT NULL,
	change_date timestamp NOT NULL default now(),
	PRIMARY KEY (cduser)
);


Create Table Slsize (
	cdsize uuid Default uuid_generate_v4(),
	nmsize varchar not null,
	
	min_size smallint not null,
	max_size smallint not null,
	PRIMARY KEY (cdsize)
);


Create Table Slrace (
	cdrace uuid Default uuid_generate_v4(),
	nmrace varchar not null default '',
	cdsize uuid REFERENCES Slsize (cdsize),
	
	strength smallint not null default 0,
	agility smallint not null default 0,
	body smallint not null default 0,
	intellect smallint not null default 0,
	wise smallint not null default 0,
	charisma smallint not null default 0,
	
	PRIMARY KEY (cdrace)
);

Create Table SlAge (
	cdage uuid Default uuid_generate_v4(),
	min_age smallint not null default 0,
	max_age smallint default 0,
	mid_age smallint
);

Create Table SLheight (
	cdheight uuid Default uuid_generate_v4(),
	nmheight varchar not null,
	min_height smallint default 0,
	max_height smallint default 0	
)



Create Table saved_hero (
	cd uuid Default uuid_generate_v4(),
	cduser uuid REFERENCES Sluser (cduser) not null,
	cdrace uuid REFERENCES Slrace (cdrace),
)



