
public class EjThreads02a implements Runnable{
	
	private int n; 
	
	public EjThreads02a (int n) {
		System.out.println("Implementando interfaz Runnable");
		this.n = n;
	}

	@Override
	public void run() {
		System.out.println("El valor inicial es: " + n);
	}
	
	public static void main(String[] args) {
		Thread t = new Thread(new EjThreads02a(5));
		t.start();
	}

}