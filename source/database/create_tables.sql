-- Create Week table
CREATE TABLE Week (
    week_id SERIAL PRIMARY KEY,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL
);

-- Create Day table
CREATE TABLE Day (
    day_id SERIAL PRIMARY KEY,
    week_id INTEGER REFERENCES Week(week_id) ON DELETE CASCADE,
    date DATE NOT NULL
);

-- Create DayPart table
CREATE TABLE DayPart (
    day_part_id SERIAL PRIMARY KEY,
    day_id INTEGER REFERENCES Day(day_id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL
);

-- Create MiniTask table
CREATE TABLE MiniTask (
    minitask_id SERIAL PRIMARY KEY,
    day_part_id INTEGER REFERENCES DayPart(day_part_id) ON DELETE CASCADE,
    description TEXT,
    task_order INTEGER
);