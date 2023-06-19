package pl.uwm.wmii.kaz.Malffy;

import java.time.LocalDate;

public class University extends School {
    private String type;
    private int studies;

    public University(String name, String address, int students, LocalDate launch, String type, int studies) {
        super(name, address, students, launch);
        if (type.equals("")) {
            this.type = "politechnika";
        } else {
            this.type = type;
        }
        if (studies < 0) {
            this.studies = 10;
        } else {
            this.studies = studies;
        }
    }

    public String getType() {
        return this.type;
    }

    public int getStudies() {
        return this.studies;
    }

    public void setType(String type) {
        if (!type.equals("")) {
            this.type = type;
        }
    }

    public void setStudies(int studies) {
        if (studies > 0) {
            this.studies = studies;
        }
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        University other = (University) o;
        return super.equals(o)
                && this.studies == other.studies;
    }

    @Override
    public String toString() {
        return super.toString()
                + this.type + this.studies;
    }

}
