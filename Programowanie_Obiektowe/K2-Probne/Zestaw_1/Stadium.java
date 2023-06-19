package pl.uwm.wmii.kaz.lemmgator;

public class Stadium extends Court {

    private String name;
    private String common_name;
    private int capacity;

    public Stadium(double width, double length, String address, int year_built, String name, String common_name, int capacity) {
        super(width, length, address, year_built);
        this.name = name;
        this.common_name = common_name;
        if (capacity < 0) capacity = 0;
        this.capacity = capacity;
    }

    public Stadium(double width, double length, String address, int year_built, String name, int capacity) {
        this(width, length, address, year_built, name, "", capacity);
    }

    public Stadium(String address, int year_built, String name) {
        this(68, 100, address, year_built, name, "", 0);
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getCommon_name() {
        return common_name;
    }

    public void setCommon_name(String common_name) {
        this.common_name = common_name;
    }

    public int getCapacity() {
        return capacity;
    }

    public void setCapacity(int capacity) {
        if (capacity < 0) capacity = 0;
        this.capacity = capacity;
    }

    @Override
    public String toString() {
        if (common_name == "") {
            return super.toString() + "\n"
                    + "Nazwa: " + getName() + ".\n"
                    + "Pojemnosc stadionu: " + getCapacity() + ".";
        } else {
            return super.toString() + "\n"
                    + "Nazwa: " + getName() + ".\n"
                    + "Nazwa zwyczajowa: " + getCommon_name() + ".\n"
                    + "Pojemnosc stadionu: " + getCapacity() + ".";
        }
    }
}