# Backend, zależności i licencje

Do implementacji zaplanowano Python i adaptery do **już działających** lokalnych usług inferencji. Kandydaci: Ollama, llama.cpp server oraz serwery udostępniające API kompatybilne z OpenAI. To plan integracji, **nie** lista zainstalowanych ani zweryfikowanych zależności.

Rdzeń powinien pozostać lekki. Transport HTTP i formaty multimodalne dobierać według rzeczywiście użytego API, nie dodawać jednocześnie wielu klientów, serwerów i modeli. Nie pakować wag, datasetów ani zewnętrznych SDK do biblioteki.

Przed integracją dostawcy wymagane są: dokumentacja API, kompatybilna licencja, wersja/digest, test błędów, limitów i prywatności, wynik na rzeczywistym lokalnym modelu. Pamięć GPU, model-router i harmonogram są odpowiedzialnością wykonawców Research Autopilot, nie biblioteki.

**Zależności runtime: brak wybranych; audyt: NOT_RUN.**
