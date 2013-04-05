package web;

public class Secenekler {
	private static  Arama_test[] commonSpecs =
	    { 
		new Arama_test("Google","http://www.google.com/search?q="),
		
	    new Arama_test("Bing","http://www.bing.com/search?q="),
	    
	    new Arama_test("Yahoo","http://search.yahoo.com/bin/search?p="),
	    
	    new Arama_test("Yandex","http://yandex.com.tr/yandsearch?lr=103833&text="),               
	      
	    };
	
	public static Arama_test[] getCommonSpecs() {
	    return(commonSpecs);
	  }
	public static String makeURL(String searchEngineName,String searchString) {
		Arama_test[] searchSpecs = getCommonSpecs();
		String searchURL = null;
		for(Arama_test spec: searchSpecs) {
			if (spec.getnm().equalsIgnoreCase(searchEngineName)) {
				searchURL = spec.makeURL(searchString);
				break;
			}
		}
		return(searchURL);
	}
}
