/*
This is a very inefficient solution.
*/
class Node {
public:
    char chr;
    bool is_word;
    vector<Node *> children;

    Node(char chr, bool is_word) : chr(chr), is_word(is_word), children() {}

    void insert(string word_slice) {
        Node *new_node = nullptr;
        bool was_found = false;
        for (auto child : children) {
            if (child->chr == word_slice[0]) {
                was_found = true;
                if (word_slice.length() > 1) {
                    child->insert(word_slice.substr(1));
                } else {
                    child->is_word = true;
                }
            }
        }
        if (!was_found) {
            Node *new_node = nullptr;
            if (word_slice.length() > 1) {
                new_node = new Node(word_slice[0], false);
                new_node->insert(word_slice.substr(1));
            } else {
                new_node = new Node(word_slice[0], true);
            }

            children.push_back(new_node);
        }
    }

    bool search(string word_slice) {
        if (word_slice.length() > 0) {
            for (auto child : children) {
                if (child->chr == word_slice[0]) {
                    return child->search(word_slice.substr(1));
                }
            }
            return false;
        }
        return is_word;
    }

    bool startsWith(string word_slice) {
        if (word_slice.length() > 0) {
            for (auto child : children) {
                if (child->chr == word_slice[0]) {
                    return child->startsWith(word_slice.substr(1));
                }
            }
            return false;
        }
        return true;
    }
};

class Trie {
public:
    vector<char> initial_letters;
    vector<Node *> children;

    Trie() : initial_letters(), children() {}

    void insert(string word) {
        bool was_found = false;
        for (auto child : children) {
            if (child->chr == word[0]) {
                was_found = true;
                if (word.length() > 1) {
                    child->insert(word.substr(1));
                } else {
                    child->is_word = true;
                }
                break;
            }
        }
        if (!was_found) {
            Node *node = nullptr;
            if (word.length() > 1) {
                node = new Node(word[0], false);
                node->insert(word.substr(1));
            } else {
                node = new Node(word[0], true);
            }
            children.push_back(node);
        }
    }

    bool search(string word) {
        for (auto child : children) {
            if (child->chr == word[0]) {
                return child->search(word.substr(1));
            }
        }
        return false;
    }

    bool startsWith(string prefix) {
        for (auto child : children) {
            if (child->chr == prefix[0]) {
                return child->startsWith(prefix.substr(1));
            }
        }
        return false;
    }
};