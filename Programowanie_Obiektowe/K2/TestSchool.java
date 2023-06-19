package pl.uwm.wmii.kaz.Malffy;


import java.time.LocalDate;


public class TestSchool {
    public static void main(String[] args) {
        School s1 = new School("Szkoła Wyższa", "ul. Zamkowa 5, 19-400 Olecko", 150, LocalDate.of(2022, 10, 20));
        School s2 = new School("Szkoła Średnia", "ul. Jeziorna 7, 19-400 Olecko", 200, LocalDate.of(2023, 9, 10));
        System.out.println(s1.getName());
        System.out.println(s1.getAddress());
        System.out.println(s1.getStudents());
        System.out.println(s1.getLaunch());
        s1.setName("szkoła wyższa");
        s1.setAddress("ul. zamkowa 5, 19-400 olecko");
        s1.setStudents(170);
        s1.setLaunch(LocalDate.of(2021, 10, 1));
        System.out.println(s1.getName());
        System.out.println(s1.getAddress());
        System.out.println(s1.getStudents());
        System.out.println(s1.getLaunch());
        System.out.println(s1);
        System.out.println(s1.equals(s2));
        System.out.println(s1.rekrutacja(50));
        University u1 = new University("Uniwersytet", "ul. Krzaczna 5, 19-400 Olecko", 300, LocalDate.of(2019, 10, 20), "rolniczy", 5);
        University u2 = new University("Uniwersytet Jakis", "ul. Olejna 5, 19-400 Olecko", 50, LocalDate.of(2017, 10, 20), "informatyczny", 8);
        System.out.println(u1.getName());
        System.out.println(u1.getAddress());
        System.out.println(u1.getStudents());
        System.out.println(u1.getLaunch());
        System.out.println(u1.getType());
        System.out.println(u1.getStudies());
        u1.setName("uniwersytet");
        u1.setAddress("ul. krzaczna 5, 19-400 olecko");
        u1.setStudents(350);
        u1.setLaunch(LocalDate.of(2020, 10, 1));
        u1.setType("medyczny");
        u1.setStudies(3);
        System.out.println(u1.getName());
        System.out.println(u1.getAddress());
        System.out.println(u1.getStudents());
        System.out.println(u1.getLaunch());
        System.out.println(u1.getType());
        System.out.println(u1.getStudies());
        System.out.println(u1);
        System.out.println(u1.equals(u2));


    }
}
