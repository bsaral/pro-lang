
public  class  ThreadTest{
  public static void main(String[] args){
  Thread th = new Thread();
  System.out.println("Say�lar 1 sn lik farkla g�steriliyor. ");
  try{
  for(int i = 1;i <= 10;i++)
    {
  System.out.println(i);
  th.sleep(1000);
  }
  }
  catch(InterruptedException e){
    System.out.println("Thread interrupted!");
  e.printStackTrace();
  }
  }
}