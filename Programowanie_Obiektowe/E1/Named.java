package pl.kmi.ujd.pliszka.zadanie1;

public interface Named {
    default String getName() {
        return "";
    }
}
