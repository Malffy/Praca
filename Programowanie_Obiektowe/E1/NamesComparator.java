package pl.kmi.ujd.pliszka.zadanie1;
import java.util.Comparator;

public class NamesComparator implements Comparator<CordlessVacuumCleaner> {
    @Override
    public int compare(CordlessVacuumCleaner c1, CordlessVacuumCleaner c2) {
        return c1.getName().compareTo(c2.getName());
    }
}
