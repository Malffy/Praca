package pl.uwm.wmii.kaz.lemmgator;

public class TestCourt {
    public static void main(String[] args) {
        Court a = new Court("Pilsudskiego", -2000);
        Court.validate(a);
        System.out.println(a.area());
        System.out.println(a);
        Stadium b = new Stadium("Słoneczna", 1999, "Słoneczniacz");
        b.setCapacity(50);
        System.out.println(b);
    }
}