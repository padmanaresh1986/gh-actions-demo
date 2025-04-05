package com.example.demo.controller;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;

@RestController
public class DemoController {

    @GetMapping("/greet")
    public String greet(){
        String unused_variable = "Test";
        String unused_variable1 = "Test";   
        String unused_variable2 = "Test";      
        return "hello world";
    }
}
