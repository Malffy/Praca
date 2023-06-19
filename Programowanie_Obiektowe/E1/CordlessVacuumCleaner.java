package pl.kmi.ujd.pliszka.zadanie1;

import java.util.Date;

public class CordlessVacuumCleaner extends VacuumCleaner implements Cloneable, Named{
    private final int id;
    private Date dateOfProd = null;

    public CordlessVacuumCleaner(String name, int id) {
        super(name);
        this.id = id;
        this.dateOfProd = new Date();
    }

    @Override
    public CordlessVacuumCleaner clone() throws CloneNotSupportedException {
        CordlessVacuumCleaner cloned = (CordlessVacuumCleaner) super.clone();
        return cloned;
    }
    public int getId() {
        return id;
    }

    @Override
    public String toString() {
        return "ID = " + id
                + ", dateOfProd = " + dateOfProd
                + "]";
    }
}
