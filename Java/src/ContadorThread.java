
public class ContadorThread extends Thread{

	private static int contador = 0;

	public void run() {

		for(int i = 0; i < 10000; i++) {
			contador++;
		}
		
	}

	public static void main(String[] args) {
		
		ContadorThread[] c = new ContadorThread[1000];

		for(int i = 0; i < c.length; i++) {
			c[i] = new ContadorThread();
			c[i].start();
		}

		System.out.println("El valor total es " + contador);
	}
}
