import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:peladas/data/data.dart';
import 'package:peladas/data/principal.dart';
import 'package:peladas/main.dart';

class loginScreen extends StatefulWidget {
  @override
  _MyCustomFormState createState() => _MyCustomFormState();
}

class _MyCustomFormState extends State<loginScreen> {
  final email = TextEditingController();
  final senha = TextEditingController();
  Api api = Api();
  final GlobalKey<ScaffoldState> _scaffoldKey = GlobalKey<ScaffoldState>();

  @override
  void dispose() {
    // Clean up the controller when the Widget is disposed
    email.dispose();
    senha.dispose();
    super.dispose();
  }

  _callSubmit(String usuario, String senha) async {
    User user = await new Api().usuario(usuario, senha);

    if (user != null) {
      Navigator.of(context).pushReplacement(
        new MaterialPageRoute(
          builder: (context) => PrincipalScreen(
                user: user,
              ),
        ),
      );
    } else {
      _scaffoldKey.currentState.showSnackBar(
        SnackBar(
          content: Text(
            "Informe login e senha corretamente",
          ),
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    final key = new GlobalKey<ScaffoldState>();

    return Scaffold(
        key: _scaffoldKey,
        appBar: AppBar(
          backgroundColor: Colors.white,
          title: Center(
            child: Text("Entrar com o email",
                style: new TextStyle(
                    color: Colors.red, fontWeight: FontWeight.normal)),
          ),
          automaticallyImplyLeading: false,
        ),
        body: Column(
          children: <Widget>[
            Padding(
              padding: EdgeInsets.all(16.0),
              child: TextFormField(
                decoration: InputDecoration(
                    labelText: 'Email',
                    fillColor: Colors.red,
                    labelStyle: TextStyle(color: Colors.red),
                    hintStyle: new TextStyle(color: Colors.red)),
                controller: email,
              ),
            ),
            Padding(
              padding: EdgeInsets.all(16.0),
              child: TextFormField(
                decoration: InputDecoration(
                    labelText: 'Senha',
                    labelStyle: TextStyle(color: Colors.red),
                    hintStyle: TextStyle(color: Colors.red)),
                controller: senha,
              ),
            ),
            new Container(
              child: Padding(
                padding: const EdgeInsets.all(16.0),
                child: InkWell(
                  onTap: () {
                    _callSubmit(email.text, senha.text);
                  },
                  child: ButtonTheme(
                    minWidth: double.infinity,
                    child: MaterialButton(
                      color: Colors.red,
                      child: Text('Entrar',
                          style: new TextStyle(
                              color: Colors.white, fontFamily: 'Heavy')),
                    ),
                  ),
                ),
              ),
            )
          ],
        ));
  }
}
