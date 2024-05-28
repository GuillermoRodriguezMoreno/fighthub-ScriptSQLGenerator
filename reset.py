def reset_file():
    with open('sql/insert_data.sql', 'w') as file:
        init_sql = """        
USE fighthub_sql;

-- CATEGORY
INSERT INTO category (name) VALUES
                                ('Professional'),
                                ('Amateur'),
                                ('Semi-Professional'),
                                ('Junior');

-- STYLE
INSERT INTO style (name) VALUES
                             ('Boxing'),
                             ('Muay Thai'),
                             ('Brazilian Jiu-Jitsu'),
                             ('Kickboxing'),
                             ('K1'),
                             ('MMA');
                             
-- ROLE
INSERT INTO role (role) VALUES
                            ('ADMIN'),
                            ('FIGHTER'),
                            ('CLUB_ADMIN');
                            
"""

        file.write(init_sql)


reset_file()
