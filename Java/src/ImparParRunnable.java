import java.util.Scanner;

public class ImparParRunnable implements Runnable{
	
	private String name;
	private int limiteSuperior;
	private int miliSeg;

	public ImparParRunnable(String name, int limiteSuperior, int miliSeg) {
		this.name = name;
		this.limiteSuperior = limiteSuperior;
		this.miliSeg = miliSeg;
	}

	public void run() {

		try {
			for(int i = 1; i <= limiteSuperior; i++) {

				if(name.equals("Impar") && i%2 == 1) {
					System.out.println("Thread " + name + " número impar: " + i);
					Thread.sleep(miliSeg);
				}else if (name.equals("Par") && i%2 == 0){
					System.out.println("Thread " + name + " número par: " + i);
					Thread.sleep(miliSeg);
				}
			}
		}
		catch(Exception e){}
	}

	public static void main(String[] args) {
		
		@SuppressWarnings("resource")
		Scanner lector = new Scanner (System.in);
		System.out.println("Ingrese el límite superior:");
		int limite = lector.nextInt();
		
		Thread impar = new Thread(new ImparParRunnable("Impar", limite, 30));
		Thread par = new Thread(new ImparParRunnable("Par", limite, 30));

		impar.start();
		par.start();

	}

}
