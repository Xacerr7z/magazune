import java.util.Random;
import java.util.Scanner;
//TIP To <b>Run</b> code, press <shortcut actionId="Run"/> or
// click the <icon src="AllIcons.Actions.Execute"/> icon in the gutter.
public class Main {
    public static void main(String[] args) {


    }
}
class Game {
    Scanner scanner = new Scanner(System.in);
    Random random = new Random();


     void menu(Pl pl) {

             System.out.println("Ты в подземелье.");

             while (pl.isAlive()) {
                 System.out.println("\nТвое HP: " + pl.getHp());
                 System.out.println("Выбери путь:");
                 System.out.println("1 — Пройти в туннель");
                 System.out.println("2 — Подняться по лестнице");

                 int choice = scanner.nextInt();

                 switch (choice) {
                     case 1:
                         monsterRoom(pl);
                         break;
                     case 2:
                         spikeTrap(pl);
                         break;
                     default:
                         System.out.println("Ты стоишь на месте, не понимая что делать.");
                 }
             }

             System.out.println("Ты погиб. Игра окончена.");
         }

         private static void monsterRoom(Pl pl) {
             System.out.println("Ты входишь в комнату. Монстр нападает!");
             fight(pl);
         }

         private static void spikeTrap(Pl pl) {
             System.out.println("Ты поднимаешься по лестнице...");
             System.out.println("ЛОВУШКА! Шипы вылетают из стен!");
             pl.takeDamage(10);
             System.out.println("Ты получил 10 урона.");
         }

         private static void fight(Pl pl) {
             Enemy enemy = new Enemy();

             while (pl.isAlive() && enemy.isAlive()) {
                 int playerDamage = pl.attack();
                 enemy.takeDamage(playerDamage);
                 System.out.println("Ты ударил монстра на " + playerDamage);

                 if (!enemy.isAlive()) {
                     System.out.println("Монстр повержен!");
                     return;
                 }

                 int enemyDamage = enemy.attack();
                 pl.takeDamage(enemyDamage);
                 System.out.println("Монстр ударил тебя на " + enemyDamage);
             }
         }
     }





class Enemy {
    private int hp = 5;

    public void takeDamage(int damage) {
        hp -= damage;
    }

    public boolean isAlive() {
        return hp > 0;
    }

    public int attack() {
        return 2;
    }

    public int getHp() {
        return hp;
    }
}


class Pl {
    private int hp;
    private final int maxHp = 20;
    private final Random random = new Random();

    public Pl() {
        this.hp = maxHp;
    }

    public int attack() {
        return random.nextInt(2) + 4; // 4–5 урона
    }

    public void takeDamage(int damage) {
        hp -= damage;
        if (hp < 0) hp = 0;
    }

    public void heal() {
        int healAmount = 5;
        hp = Math.min(hp + healAmount, maxHp);
        System.out.println("Ты восстановил " + healAmount + " HP.");
    }

    public boolean isAlive() {
        return hp > 0;
    }

    public int getHp() {
        return hp;
    }
}
