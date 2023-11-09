CREATE TABLE people (
    id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    mobile TEXT,
    email TEXT
);

CREATE TABLE users (
    people_id INTEGER PRIMARY KEY,
    username text NOT NULL UNIQUE,
    hash text NOT NULL UNIQUE,
    FOREIGN KEY (people_id) REFERENCES people(id)
);

CREATE TABLE companies (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    people_id INTEGER,
    category TEXT NOT NULL,
    balance_paisa INTEGER DEFAULT 0,
    FOREIGN KEY (people_id) REFERENCES people(id)
);

CREATE TABLE address (
    company_id INTEGER PRIMARY KEY,
    unit TEXT,
    block TEXT,
    street TEXT,
    city TEXT,
    FOREIGN KEY (company_id) REFERENCES companies(id)
);

CREATE TABLE publishers (
    id INTEGER PRIMARY KEY,
    companies_id INTEGER NOT NULL,
    FOREIGN KEY (companies_id) REFERENCES companies(id)
);

CREATE TABLE books (
    id INTEGER PRIMARY KEY,
    publisher_id INTEGER NOT NULL,
    title TEXT NOT NULL,
    edition TEXT,
    year_of_publishing TEXT,
    pages INTEGER,
    colours INTEGER,
    binding TEXT,
    times_printed INTEGER,
    FOREIGN KEY (publisher_id) REFERENCES publishers(id)
);

/* Loaded Up to Here */

CREATE TABLE plate_suppliers(
    id INTEGER PRIMARY KEY,
    companies_id INTEGER NOT NULL,
    FOREIGN KEY (companies_id) REFERENCES companies(id)
);

CREATE TABLE binders(
    id INTEGER PRIMARY KEY,
    companies_id INTEGER NOT NULL,
    FOREIGN KEY (companies_id) REFERENCES companies(id)
);

CREATE TABLE printers(
    id INTEGER PRIMARY KEY,
    companies_id INTEGER NOT NULL,
    FOREIGN KEY (companies_id) REFERENCES companies(id)
);

CREATE TABLE paper_suppliers(
    id INTEGER PRIMARY KEY,
    companies_id INTEGER NOT NULL,
    FOREIGN KEY (companies_id) REFERENCES companies(id)
);

CREATE TABLE paper (
    batch_no INTEGER PRIMARY KEY,
    paper_suppliers_id INTEGER NOT NULL,
    size TEXT,
    type TEXT NOT NULL,
    bought_rate INTEGER NOT NULL,
    market_rate INTEGER,
    country TEXT,
    stock_reams INTEGER NOT NULL,
    FOREIGN KEY (paper_suppliers_id) REFERENCES paper_suppliers(id)
);


CREATE TABLE plates (
    id INTEGER PRIMARY KEY,
    plates_supplier_id INTEGER NOT NULL,
    book_id INTEGER NOT NULL,
    type TEXT,
    size TEXT,
    bought_rate INTEGER NOT NULL,
    scrap_rate INTEGER,
    quantity INTEGER,
    times_repeated INTEGER,
    FOREIGN KEY (plates_supplier_id) REFERENCES plate_suppliers(id)
);

CREATE TABLE orders (
    id INTEGER PRIMARY KEY,
    date NUMERIC NOT NULL,
    book_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    plates_unit_cost INTEGER NOT NULL,
    binding_unit_cost INTEGER NOT NULL,
    paper_unit_cost INTEGER NOT NULL,
    batch_no INTEGER NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (book_id) REFERENCES book(id),
    FOREIGN KEY (batch_no) REFERENCES paper(batch_no)
);

CREATE TABLE ordered_plates (
    orders_id INTEGER NOT NULL,
    plates_id INTEGER NOT NULL,
    FOREIGN KEY (orders_id) REFERENCES orders(id),
    FOREIGN KEY (plates_id) REFERENCES plates(id)
);

CREATE TABLE bind_job (
    orders_id INTEGER PRIMARY KEY,
    binders_id INTEGER NOT NULL,
    type TEXT,
    rate INTEGER NOT NULL,
    FOREIGN KEY (orders_id) REFERENCES orders(id),
    FOREIGN KEY (binders_id) REFERENCES binders(id)
);

CREATE TABLE print_jobs (
    id INTEGER PRIMARY KEY,
    printers_id INTEGER NOT NULL,
    type TEXT,
    size TEXT,
    colour TEXT,
    rate INTEGER,
    notes TEXT,
    approval INTEGER,
    FOREIGN KEY (printers_id) REFERENCES printers(id)
);

CREATE TABLE ordered_priting (
    print_job_id INTEGER PRIMARY KEY,
    orders_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    FOREIGN KEY (print_job_id) REFERENCES print_jobs(id),
    FOREIGN KEY (orders_id) REFERENCES orders(id)
);

CREATE TABLE invoices (
    id INTEGER PRIMARY KEY,
    date_issue NUMERIC NOT NULL,
    total INTEGER,
    status TEXT NOT NULL,
    date_paid NUMERIC
);