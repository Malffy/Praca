package pl.uwm.wmii.kaz.Malffy;

import java.time.LocalDate;

class School {
    private String name;
    private String address;
    private int students;
    private LocalDate launch;

    public School(String name, String address, int students, LocalDate launch) {
        if (name.equals("")) {
            this.name = "Wydział Matematki i Informatyki UWM";
        } else {
            this.name = name;
        }
        if (address.equals("")) {
            this.address = "ul. Słoneczna 54, 10-710 Olsztyn";
        } else {
            this.address = name;
        }
        if (students < 0) {
            this.students = 100;
        } else {
            this.students = students;
        }
        this.launch = launch;
        if (launch.isAfter(launch.getChronology().dateNow())) {
            this.launch = launch.getChronology().dateNow();
        } else {
            this.launch = launch;
        }
    }

    public String getName() {
        return this.name;
    }

    public String getAddress() {
        return this.address;
    }

    public int getStudents() {
        return this.students;
    }

    public LocalDate getLaunch() {
        return this.launch;
    }

    public void setName(String name) {
        if (!name.equals("")) {
            this.name = name;
        }
    }


    public void setAddress(String address) {
        if (!address.equals("")) {
            this.address = address;
        }
    }

    public void setStudents(int students) {
        if (students > 0) {
            this.students = students;
        }
    }

    public void setLaunch(LocalDate launch) {
        if (!launch.isAfter(launch.getChronology().dateNow())) {
            this.launch = launch;
        }
    }

    @Override
    public String toString() {
        return getClass().getSimpleName() + this.name + this.address + this.students + this.launch;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        School other = (School) o;
        return this.address.equals(other.address);
    }

    public int rekrutacja (int a){
        this.students = this.students+a;
        if(students>500){
            this.students =500;
        }
        return this.students;
    }
}
