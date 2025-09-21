import java.util.Scanner;

public class VentasDepartamentos {
    static String[] departamentos = {"Ropa", "Deportes", "Juguetería"};
    static String[] meses = {"Enero","Febrero","Marzo","Abril","Mayo","Junio",
                             "Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"};

    static double[][] ventas = new double[departamentos.length][meses.length];
    static Scanner sc = new Scanner(System.in);

    // Insertar venta
    public static void insertarVenta() {
        System.out.println("Seleccione el departamento:");
        for (int i = 0; i < departamentos.length; i++) {
            System.out.println(i + " - " + departamentos[i]);
        }
        int depto = sc.nextInt();

        System.out.println("Seleccione el mes (0=Enero ... 11=Diciembre):");
        int mes = sc.nextInt();

        System.out.print("Ingrese la venta: ");
        double monto = sc.nextDouble();

        ventas[depto][mes] = monto;
        System.out.println("Venta registrada con éxito.");
    }

    // Buscar venta por monto
    public static void buscarVenta() {
        System.out.print("Ingrese el monto a buscar: ");
        double monto = sc.nextDouble();

        boolean encontrado = false;
        for (int i = 0; i < departamentos.length; i++) {
            for (int j = 0; j < meses.length; j++) {
                if (ventas[i][j] == monto) {
                    System.out.println("Encontrado $" + monto + " en " + departamentos[i] + " - " + meses[j]);
                    encontrado = true;
                }
            }
        }
        if (!encontrado) {
            System.out.println("No se encontró la venta.");
        }
    }

    // Eliminar venta
    public static void eliminarVenta() {
        System.out.println("Seleccione el departamento:");
        for (int i = 0; i < departamentos.length; i++) {
            System.out.println(i + " - " + departamentos[i]);
        }
        int depto = sc.nextInt();

        System.out.println("Seleccione el mes (0=Enero ... 11=Diciembre):");
        int mes = sc.nextInt();

        ventas[depto][mes] = 0;
        System.out.println("Venta eliminada correctamente.");
    }

    // Mostrar todas las ventas
    public static void mostrarVentas() {
        for (int i = 0; i < departamentos.length; i++) {
            System.out.print(departamentos[i] + ": ");
            for (int j = 0; j < meses.length; j++) {
                System.out.print(meses[j] + "=" + ventas[i][j] + " | ");
            }
            System.out.println();
        }
    }

    public static void main(String[] args) {
        int opcion;
        do {
            System.out.println("\n--- Menú ---");
            System.out.println("1. Insertar venta");
            System.out.println("2. Buscar venta");
            System.out.println("3. Eliminar venta");
            System.out.println("4. Mostrar todas las ventas");
            System.out.println("0. Salir");
            System.out.print("Opción: ");
            opcion = sc.nextInt();

            switch (opcion) {
                case 1: insertarVenta(); break;
                case 2: buscarVenta(); break;
                case 3: eliminarVenta(); break;
                case 4: mostrarVentas(); break;
                case 0: System.out.println("Saliendo..."); break;
                default: System.out.println("Opción inválida.");
            }
        } while (opcion != 0);
    }
}
