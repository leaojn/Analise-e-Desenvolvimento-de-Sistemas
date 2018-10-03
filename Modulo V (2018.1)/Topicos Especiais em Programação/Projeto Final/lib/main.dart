import 'dart:convert';

import 'package:flutter/material.dart';
import 'package:http/http.dart';
import 'package:http/http.dart' as http;
import 'package:peladas/data/data.dart';
import 'package:peladas/data/principal.dart';
import 'package:peladas/login.dart';
import 'dart:async';
import 'package:shared_preferences/shared_preferences.dart';

void main() {
  runApp(MaterialApp(
    title: 'Navigation Basics',
    home: MyApp(),
    theme: ThemeData(
        brightness: Brightness.light,
        primaryColor: Colors.red,
        accentColor: Colors.white),
  ));
}

class MyApp extends StatefulWidget {
  @override
  MyAppState createState() => MyAppState();
}

class MyAppState extends State<MyApp> {
  Api api = Api();
  User _user;
  bool _login;
  String _token;

  Widget _buildNameWidget(String text) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 2.0),
      child: Text(
        text,
        style: TextStyle(fontWeight: FontWeight.bold),
      ),
    );
  }

  initState() {
    _preferencs();
  }

  Widget icons() {
    return IconButton(
      icon: Icon(Icons.people_outline),
      color: Colors.red,
      onPressed: () {
        if (_token != null) {
          print(_user.username);
          Navigator.push(
            context,
            MaterialPageRoute(
                builder: (context) => PrincipalScreen(
                      user: _user,
                    )),
          );
        } else {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => loginScreen()),
          );
        }
      },
    );

    // else {
    //   return IconButton(
    //     icon: Icon(Icons.access_time),
    //     color: Colors.red,
    //     onPressed: () {
    //       print(_token);
    //       setState(() {
    //         _login = false;
    //       });
    //       // Navigator.push(
    //       //   context,
    //       //   MaterialPageRoute(builder: (context) => loginScreen()),
    //       // );
    //     },
    //   );
    // }
  }

  _preferencs() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('token');
    if (token == null) {
      _login = false;
    } else {
      User result = await new Api().loginWithToken(token);

      setState(() {
        _token = token;
        _user = result;
      });
    }
    //  else {
    //   print(_login);
    //   User result = await new Api().loginWithToken(token);
    //   setState(() {
    //     _user = result;
    //     _login = true;
    //   });
    // }
  }

  Widget _iconWidget() {
    return Icon(Icons.score);
  }

  @override
  Widget build(BuildContext context) {
    return new Scaffold(
      appBar: new AppBar(
        backgroundColor: Colors.white,
        title: Center(
          child: new Text("Peladas API",
              style: new TextStyle(
                  color: Colors.red, fontWeight: FontWeight.normal)),
        ),
        actions: <Widget>[
          // _preferencs(),
          icons(),
        ],
      ),
      body: new Container(
        child: new FutureBuilder<List<Pelada>>(
          future: api.getPeladas(),
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return new ListView.builder(
                  itemCount: snapshot.data.length,
                  itemBuilder: (context, index) {
                    return new Card(
                        child: new Column(
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: <Widget>[
                        SizedBox(
                          width: double.infinity,
                          child: Image.network(
                              "https://conteudo.imguol.com.br/c/esporte/6c/2017/09/06/neymar-e-mbappe-se-encontram-pela-primeira-vez-em-treino-do-psg-1504716753721_615x300.jpg"),
                        ),
                        Container(
                          padding: EdgeInsets.all(20.0),
                          child: Row(
                            mainAxisAlignment: MainAxisAlignment.spaceBetween,
                            crossAxisAlignment: CrossAxisAlignment.center,
                            children: <Widget>[
                              _buildNameWidget(snapshot.data[index].nome),
                              _iconWidget()
                            ],
                          ),
                        ),
                      ],
                    ));
                  });
            } else if (snapshot.hasError) {
              return new Text("${snapshot.error}");
            }

            // By default, show a loading spinner
            return new CircularProgressIndicator();
          },
        ),
      ),
    );
  }
}

Future<String> getToken() async {
  final prefs = await SharedPreferences.getInstance();
  String token = prefs.getString('token');
  return token;
}

Future<String> fetchUsersFromGitHub(String username, String senha) async {
  Map<String, String> body = {"username": username, "password": senha};

  final response =
      await http.post('http://192.168.137.1:4000/api/login', body: body);
  String t = json.decode(response.body.toString())["token"].toString();
  if (response.statusCode == 200) {
    String t = json.decode(response.body.toString())["token"].toString();
    final preferencs = (await SharedPreferences.getInstance());
    preferencs.setString("token", t);

    return t;
  } else {
    return "false";
  }
}

class Api {
  static const String DEV_ENDPOINT = 'http://192.168.137.1:4000/';
  static const String API_ENDPOINT = 'api/';
  Future<String> getToken() async {
    final prefs = await SharedPreferences.getInstance();
    final token = prefs.getString('token');
    return token;
  }

  Future putConfiguracao(
      String token,
      int id,
      String tempos,
      String tempo_duracao,
      String limite_gols,
      String qtd_jogadores,
      String tipo_sorteio) async {
    String url = DEV_ENDPOINT + API_ENDPOINT + 'configuracao/' + id.toString();
    Map<String, String> body = {
      "id": id.toString(),
      "tempos": tempos,
      "tempo_duracao": tempo_duracao,
      "limite_gols": limite_gols,
      "qtd_jogadores": qtd_jogadores,
      "tipo_sorteio": tipo_sorteio,
    };
    final response = await http
        .put(url, body: body, headers: {'authorization': "Token " + token});
    print(response.body);
  }

  Future<PeladaDetalhe> peladaDetalhe(String token, int id) async {
    String url = DEV_ENDPOINT + API_ENDPOINT + 'pelada/' + id.toString();
    final response =
        await http.get(url, headers: {'authorization': "Token " + token});
    var data = json.decode(response.body.toString());
    String nome = data["nome"];
    String username = data["dono"]["username"];
    String email = data["dono"]["email"];
    Dono dono = Dono(username: username, email: email);
    var jogadores = json.decode(response.body)['jogadores'];

    // var e = data['email'] ?? "null";
    // print(data['jogadores']);
    List<Jogador> players = new List();
    for (var j in jogadores) {
      Jogador jogador = new Jogador(
          id: j['id'] ?? "null",
          nome: j['nome'] ?? "null",
          rating: j['rating'] ?? "null",
          email: j['email'] ?? "null");
      players.add(jogador);
    }
    PeladaDetalhe peladaDetalhe = new PeladaDetalhe(
        nome: nome, dono: dono, jogadores: players, id: data['id']);
    return peladaDetalhe;
  }

  Future<User> loginWithToken(String token) async {
    Response r = await get(DEV_ENDPOINT + API_ENDPOINT + "user/",
        headers: {'authorization': "Token " + token});
    int id = (json.decode(r.body)["id"]);
    String user = (json.decode(r.body)["username"]);
    String email = ((json.decode(r.body)["email"]));
    User u = new User(id: id, username: user, email: email);
    final preferencs = (await SharedPreferences.getInstance());
    preferencs.setString("nome", user);
    preferencs.setString("email", email);
    preferencs.setString("token", token);
    if (r.statusCode == 200) {
      return u;
    } else {
      return null;
    }
  }

  Future<User> usuario(String username, String password) async {
    Map<String, String> body = {"username": username, "password": password};
    final response =
        await http.post(DEV_ENDPOINT + API_ENDPOINT + 'login', body: body);
    String token = json.decode(response.body.toString())["token"].toString();
    Response r = await get(DEV_ENDPOINT + API_ENDPOINT + "user/",
        headers: {'authorization': "Token " + token});
    int id = (json.decode(r.body)["id"]);
    String user = (json.decode(r.body)["username"]);
    String email = ((json.decode(r.body)["email"]));
    User u = new User(id: id, username: user, email: email);
    final preferencs = (await SharedPreferences.getInstance());
    preferencs.setString("nome", user);
    preferencs.setString("email", email);
    preferencs.setString("token", token);
    if (response.statusCode == 200) {
      return u;
    } else {
      return null;
    }
  }

  Future<bool> postJogador(
      String nome, int rating, String pelada, String token) async {
    Map<String, String> body = {
      "nome": nome,
      "rating": rating.toString(),
      "pelada": pelada.toString()
    };

    final response = await http.post(DEV_ENDPOINT + API_ENDPOINT + 'jogadores/',
        body: body, headers: {'Authorization': "Token " + token});
    if (response.statusCode == 201) {
      return true;
    }
    return false;
  }

  Future<bool> deleteJogador(int id, String token) async {
    final response = await http.delete(
        DEV_ENDPOINT + API_ENDPOINT + 'jogador/' + id.toString(),
        headers: {'Authorization': "Token " + token});
    if (response.statusCode == 204) {
      return true;
    }
    return false;
  }

  Future<List<Pelada>> userPeladas(String token) async {
    Response r = await get(DEV_ENDPOINT + API_ENDPOINT + "user-peladas/",
        headers: {'Authorization': "Token " + token});
    if (r.statusCode == 200) {
      List responseJson = json.decode(r.body.toString());
      List<Pelada> userList = createPeladaList(responseJson);
      return userList;
    } else {
      return;
    }
  }

  Future<Configuracao> getConfiguracao(String token, int id) async {
    Response r = await get(
        DEV_ENDPOINT +
            API_ENDPOINT +
            "pelada/" +
            id.toString() +
            '/configuracao',
        headers: {'Authorization': "Token " + token});
    if (r.statusCode == 200) {
      var responseJson = json.decode(r.body.toString());
      var tempos = responseJson['tempos'];
      var tempo_duracao = responseJson['tempo_duracao'];
      var id = responseJson['id'];
      var limite_gols = responseJson['limite_gols'];
      var qtd_jogadores = responseJson['qtd_jogadores'];
      var tipo_sorteio = responseJson['tipo_sorteio'];
      Configuracao configuracao = new Configuracao(
          id: id,
          tempos: tempos,
          tempo_duracao: tempo_duracao,
          limite_gols: limite_gols,
          qtd_jogadores: qtd_jogadores,
          tipo_sorteio: tipo_sorteio);
      return configuracao;
    } else {
      return;
    }
  }

  Future<List<Pelada>> getPeladas() async {
    final String url = DEV_ENDPOINT + API_ENDPOINT + "peladas/";
    final response = await http.get(url);
    if (response.statusCode == 200) {
      List responseJson = json.decode(response.body.toString());
      List<Pelada> userList = createPeladaList(responseJson);
      return userList;
    } else {
      return;
    }
  }
}

List<Pelada> createPeladaList(List data) {
  List<Pelada> list = new List();
  for (int i = 0; i < data.length; i++) {
    var id = data[i]["id"];
    var name = data[i]['nome'];
    var dono = data[i]["dono"];
    var tempos = data[i]["configuracao"]["tempos"];
    var conf_id = data[i]["configuracao"]["id"];
    var tempo_duracao = data[i]["configuracao"]["tempo_duracao"];
    var limite_gols = data[i]["configuracao"]["limite_gols"];
    var qtd_jogadores = data[i]["configuracao"]["qtd_jogadores"];
    var tipo_sorteio = data[i]["configuracao"]["tipo_sorteio"];

    Configuracao configuracao = new Configuracao(
        id: conf_id,
        tempos: tempos,
        tempo_duracao: tempo_duracao,
        limite_gols: limite_gols,
        qtd_jogadores: qtd_jogadores,
        tipo_sorteio: tipo_sorteio);

    Pelada pelada =
        new Pelada(id: id, nome: name, configuracao: configuracao, dono: dono);
    list.add(pelada);
  }
  return list;
}
