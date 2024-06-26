from Operations.QuerySystem import QuerySystem
from Operations.IndexInverter import InvertedIndex
from Compression.Compressor import Compressor
from time import sleep, time
import random

def printResult(query, result, start_time):
    print("\n------------------------------------------------\n")
    print(f"Query: {query}")
    # sleep(0.1)
    print("\nProcessing the Query...")
    # sleep(0.5)
    print("Process Completed!")
    print("\nResults:")
    # sleep(0.5)
    print("Documents: ", result)
    print()
    end_time = time()
    print("Time taken:", end_time - start_time, "seconds")
    print("\n------------------------------------------------\n")
    sleep(1)

def main():
    documents = {
        1: "In recent years, artificial intelligence (AI) has revolutionized various industries.",
        2: "Machine learning, a subset of AI, enables computers to learn from data and improve over time.",
        3: "Natural language processing (NLP) is a branch of AI that focuses on the interaction between computers and humans through language.",
        4: "Data science is an interdisciplinary field that extracts knowledge and insights from structured and unstructured data.",
        5: "The Internet of Things (IoT) refers to the network of physical objects embedded with sensors, software, and other technologies for connecting and exchanging data.",
        6: "Blockchain technology, originally devised for the digital currency Bitcoin, is a distributed ledger system that securely records transactions across multiple computers.",
        7: "Quantum computing leverages the principles of quantum mechanics to perform computations at speeds exponentially faster than classical computers.",
        8: "Cybersecurity encompasses practices, technologies, and processes designed to protect computer systems, networks, and data from unauthorized access or attacks.",
        9: "Renewable energy sources such as solar, wind, and hydroelectric power are becoming increasingly important in addressing environmental concerns and reducing dependence on fossil fuels.",
        10: "Biotechnology is the application of biological processes, organisms, or systems to develop products and technologies that improve human health and the environment."
    }

    wordDict = [f"word{i}" for i in range(1000)]

    randomPairs = [(random.choice(wordDict), random.randint(1, 10000)) for _ in range(1000000)]

    invertedIndex = InvertedIndex()
    invertedIndex.buildIndex(documents=documents)

    querySystem = QuerySystem(invertedIndex)

    while True:
        try:
            print("\n------------------------------------------------\n")
            userInput = input("Do you want to search for a term? (yes/no): ").lower()
            if userInput == "yes":
                term = input("Enter the query you want to search for: ")
                start_time = time()
                result = querySystem.processQuery(term)
                if result:
                    printResult(term, result, start_time)
                else:
                    print("\nNo documents found for the term.\n")
                    continue
            elif userInput == "no":
                print("\nDo you want to:")
                print("1. Exit the program")
                print("2. See the results of default queries")
                choice = input("Enter your choice (1/2): ")
                if choice == "1":
                    break
                elif choice == "2":
                    print("\nSearching for predefined queries...")
                    queries = [
                        "artificial",
                        "intelligence",
                        "artificial AND intelligence",
                        "machine",
                        "machine AND learning",
                        "data AND science",
                        "biotechnology OR renewable OR energy"
                    ]
                    for query in queries:
                        start_time = time()
                        result = querySystem.processQuery(query)
                        printResult(query, result, start_time)
                else:
                    raise ValueError("\nInvalid choice. Please enter '1' or '2'.\n")
            else:
                raise ValueError("\nInvalid input. Please enter 'yes' or 'no'.\n")
        except ValueError as ve:
            print(ve)

    print("\n------------------------------------------------\n")
    sleep(1)
    print("\nTesting Compression...\n")

    print("Creating Inverted Index...")
    sleep(1)
    print("Inverted Index Created Successfully!\n")
    sleep(1)
    print("Randomly adding 1000 words and 1000 document IDs to the Inverted Index...\n")
    sleep(1)
    print("Compressing the Inverted Index...\n")

    # print(f"Random Pairs: {randomPairs}...")

    for word, docID in randomPairs:
        invertedIndex.invertedIndex[word].add(docID)

    for term, docIDs in invertedIndex.invertedIndex.items():
        print(f"Term: {term}")
        print(f"Original DocIDs: {docIDs}")
        compressedGamma = invertedIndex.compress(docIDs, method="gamma")
        compressedFibonacci = invertedIndex.compress(docIDs, method="fibonacci")

        print(f"Gamma Encoded: {compressedGamma}")
        print(f"Fibonacci Encoded: {compressedFibonacci}")
        print()

    print("\nExiting the Program...")
    sleep(2)
    print("Program Exited!")

if __name__ == "__main__":
    main()
