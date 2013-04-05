package web;

public class Arama_test {
	private String name ,  URL ;
	
	public Arama_test(String name,String URL) {
		this.name = name;
		this.URL = URL ;
		
	}
	
	public String makeURL (String searchURL){
		return(URL+searchURL);
	}
	
	public String getnm (){
		return (name);
	}
}
