package pl.kmi.ujd.pliszka.zadanie1;

import java.util.ArrayList;

public class Zadanie2 {
    public static <T extends Comparable<T>> T max(ArrayList<T> list) {
        T max = list.get(0);
        for (T t : list) {
            if (t.compareTo(max) > 0) {
                max = t;
            }
        }
        return max;
    }
}