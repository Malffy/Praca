package pl.uwm.wmii.kaz.lemmgator;
public class Main {
    public static void main(String[] args) {
        Mebel maly = new Mebel("Maly Mebel", 1, 0.5, 4);
        System.out.println(maly);
        System.out.println(Mebel.getIle());
        Mebel sredni = new Mebel(2, 1, 4);
        System.out.println(sredni);
        Biurko maleBiurko = new Biurko("Male Biurko", 2, 1, 4, 22);
        maleBiurko.setDataProdukcji(2005, 2, 28);
        System.out.println(maleBiurko);
        System.out.println(Mebel.getIle());
        Mebel[][] spis = new Mebel[2][2];
        spis[0][0] = sredni;
        spis[1][0] = maly;
        spis[0][1] = maleBiurko;
        spis[1][1] = sredni;
        String[] spisNazw = new String[4];
        spisNazw[0] = sredni.getNazwa();
        spisNazw[1] = maly.getNazwa();
        spisNazw[2] = maleBiurko.getNazwa();
        spisNazw[3] = sredni.getNazwa();
        for(String i: spisNazw) {
            System.out.println(i);
        }
        System.out.println(sredni.equals(maly));
        System.out.println(sredni.equals(maleBiurko));

        int licz = 0;
        for(int i = 0; i < spis.length; i++) {
            for(int j = 0; j < spis[i].length; j++) {
                if(spis[i][j].getClass() == Biurko.class){
                    licz++;
                }
            }
        }
        System.out.println(licz);

        StringBuilder w = new StringBuilder("");
        for(int i = 0; i < spis.length; i++) {
            for(int j = 0; j < spis[i].length; j++) {
                w.append(spis[i][j].getNazwa());
                if(i != spis.length - 1 || j != spis[i].length - 1){
                    w.append(", ");
                }
            }
        }
        System.out.println(w);
    }
}