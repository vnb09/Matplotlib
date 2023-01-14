/*
 * Counting duplicate characters: Write a program that counts duplicate characters 
 * from a given string.
*/

import java.util.HashMap;
import java.util.Map;

public class p1{
    public static void main(String[] args){
        String str = "jiggle jiggle";
        countchars(str);
    }

    public static void countchars(String str){
        HashMap<Character, Integer> hm = new HashMap<>();
        for(int i = 0; i < str.length(); i++){
            char c = str.charAt(i);
            if(!(hm.containsKey(c)))
            hm.put(c, 1);

            else
            hm.put(c, hm.get(c) + 1);
        }

        for(Map.Entry en: hm.entrySet())
        System.out.println(en.getKey()+" "+en.getValue());
    }
}
