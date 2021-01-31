
public class EjThreads02 implements Runnable{

	@Override
	public void run() {
		System.out.println("Implementando interfaz Runnable");
	}
	
	public static void main(String[] args) {
		Thread t = new Thread(new EjThreads02());
		t.start();
	}

}
