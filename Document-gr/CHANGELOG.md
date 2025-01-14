# Αρχείο καταγραφής αλλαγών (Changelog)

## V1.3.1 και νεότερη έκδοση

Όλα τα Changelog μας είναι διαθέσιμα στο διαδίκτυο στο Github repo OWASP MASVS, ανατρέξτε στo [Releases page](https://github.com/OWASP/owasp-masvs/releases).

## V1.3 - 13 Μαΐου 2021

Είμαστε περήφανοι που ανακοινώνουμε την εισαγωγή ενός document build pipeline, ο οποίος αποτελεί σημαντικό ορόσημο για το έργο μας. Το build pipeline βασίζεται στο [Pandocker](https://github.com/dalibo/pandocker) και στο [Github Actions](https://github.com/OWASP/owasp-masvs/tree/master/.github/workflows ).
Αυτό μειώνει σημαντικά τον χρόνο που δαπανάται για τη δημιουργία νέων εκδόσεων και θα αποτελέσει επίσης τη βάση για το OWASP MSTG και θα διατεθεί για το έργο OWASP ASVS.

### Αλλαγές

- Υπάρχουν διαθέσιμες 4 ακόμη μεταφράσεις, οι οποίες είναι Hindi, Farsi, Πορτογαλικά και Πορτογαλικά Βραζιλίας
- Προστέθηκε η απαίτηση MSTG-PLATFORM-11

### Ιδιαίτερες ευχαριστίες

- Το Jeroen Willemsen για την έναρξη αυτής της πρωτοβουλίας πέρυσι!
- Το Damien Clochard και το Dalibo για την υποστήριξη και την επαγγελματοποίηση του build pipeline.
- Όλοι οι Hindi, Farsi, Πορτογάλοι και Βραζιλιάνοι συνεργάτες μας για την εξαιρετική μεταφραστική δουλειά.

## V1.2 - 7 Μαρτίου 2020 - Διεθνής κυκλοφορία

Οι ακόλουθες αλλαγές αποτελούν μέρος της έκδοσης 1.2:

- Διατίθεται μετάφραση του MASVS στα απλοποιημένα κινέζικα.
- Αλλαγή τίτλου στο εξώφυλλο του βιβλίου MASVS.
- Αφαιρέθηκε το Mobile Top 10 και το CWE από το MSTG και συγχωνεύτηκαν σε υπάρχουσες αναφορές στο MASVS.

## V1.2-RC - 5 Οκτωβρίου 2019 - Προέκδοση (μόνο στα Αγγλικά)

Οι ακόλουθες αλλαγές αποτελούν μέρος της προέκδοσης 1.2:

- Προαγωγή σε flagship status.
- Η απαίτηση άλλαξε: MSTG-STORAGE-1 "πρέπει να χρησιμοποιηθεί".
- Προστίθενται οι απαιτήσεις MSTG-STORAGE-13, MSTG-STORAGE-14 και MSTG-STORAGE-15 με έμφαση στην προστασία δεδομένων.
- Η απαίτηση MSTG-AUTH-11 ενημερώθηκε για τη διατήρηση των συναφών πληροφοριών.
- Η απαίτηση MSTG-CODE-4 ενημερώθηκε για να καλύπτει περισσότερα από απλώς το debugging.
- Η απαίτηση MSTG-PLATFORM-10 προστέθηκε για την περαιτέρω ασφαλή χρήση των WebViews.
- Η απαίτηση MSTG-AUTH-12 προστέθηκε για να υπενθυμίζει στους προγραμματιστές την εφαρμογή εξουσιοδοτήσεων, ειδικά στην περίπτωση εφαρμογών πολλών χρηστών.
- Προστέθηκε λίγη περισσότερη περιγραφή για το πώς θα πρέπει να χρησιμοποιείται το MASVS με βάση την αξιολόγηση κινδύνου.
- Προστέθηκε λίγη περισσότερη περιγραφή για το περιεχόμενο επί πληρωμή.
- Η απαίτηση MSTG-ARCH-11 προστέθηκε για να συμπεριλάβει μια πολιτική Υπεύθυνης Αποκάλυψης (ΝDA) για εφαρμογές L2.
- Η απαίτηση MSTG-ARCH-12 προστέθηκε για να δείξει στους προγραμματιστές εφαρμογών ότι πρέπει να τηρούνται οι σχετικοί διεθνείς νόμοι περί απορρήτου και ιδιωτικότητας.
- Δημιούργησε ένα συνεπές στυλ για όλες τις αναφορές στην αγγλική έκδοση.
- Η απαίτηση MSTG-PLATFORM-11 προστέθηκε για την καταπολέμηση της κατασκοπείας μέσω πληκτρολογίων τρίτων.
- Η απαίτηση MSTG-MSTG-RESILIENCE-13 προστέθηκε για να εμποδίσει την υποκλοπή σε μια εφαρμογή.

## V1.1.4 - 4 Ιουλίου 2019 - Έκδοση summit

Οι ακόλουθες αλλαγές αποτελούν μέρος της έκδοσης 1.1.4:

- Διορθώθηκαν όλα τα ζητήματα σήμανσης.
- Ενημερώσεις στη γαλλική και ισπανική μετάφραση.
- Μεταφράστηκε το αρχείο καταγραφής αλλαγών (changelog) στα Κινέζικα (ZHTW) και στα Ιαπωνικά.
- Αυτοματοποιημένη επαλήθευση της σύνταξης σήμανσης και της προσβασιμότητας των διευθύνσεων URL.
- Προστέθηκαν κωδικοί αναγνώρισης στις απαιτήσεις, οι οποίοι θα συμπεριληφθούν στη μελλοντική έκδοση του MSTG για να βρίσκετε εύκολα τις συστάσεις και τις δοκιμαστικές περιπτώσεις.
- Μειώθηκε το μέγεθος του repo και προστέθηκε το Generated στο .gitignore.
- Προστέθηκε ένας Κώδικας Δεοντολογίας & Οδηγίες Συνεισφοράς.
- Προστέθηκε ένα πρότυπο Pull-Request.
- Ενημερώθηκε ο συγχρονισμός με το repo που χρησιμοποιείται για τη φιλοξενία του ιστότοπου Gitbook.
- Ενημερώθηκαν τα σενάρια για τη δημιουργία XML/JSON/CSV για όλες τις μεταφράσεις.
- Μεταφράστηκε ο Πρόλογος στα Κινέζικα (ZHTW).

## V1.1.3 - 9 Ιανουαρίου 2019 - Μικρές διορθώσεις

- Διορθώστε το ζήτημα μετάφρασης της απαίτησης 7.1 στην ισπανική έκδοση
- Νέα ρύθμιση μεταφραστών σε ευχαριστίες

## V1.1.2 - 3 Ιανουαρίου 2019 - Χορηγία και διεθνοποίηση

Οι ακόλουθες αλλαγές αποτελούν μέρος της έκδοσης 1.1.2:

- Προστέθηκε ευχαριστήριο σημείωμα για τους αγοραστές του ηλεκτρονικού βιβλίου.
- Προστέθηκε σύνδεσμος ελέγχου ταυτότητας που λείπει και ενημερώθηκε ο κατεστραμμένος σύνδεσμος ελέγχου ταυτότητας στο V4.
- Διορθώθηκε το swap μεταξύ 4.7 και 4.8 στα Αγγλικά.
- Πρώτη διεθνής κυκλοφορία!
  - Διορθώσεις σε ισπανική μετάφραση. Η μετάφραση είναι πλέον σε συγχρονισμό με τα Αγγλικά (1.1.2).
  - Διορθώσεις σε ρωσική μετάφραση. Η μετάφραση είναι πλέον σε συγχρονισμό με τα Αγγλικά (1.1.2).
  - Προστέθηκε η πρώτη κυκλοφορία των Κινεζικών (ZHTW) Γαλλικών, Γερμανικών και Ιαπωνικών!
- Απλοποιημένο έγγραφο για ευκολία στη μετάφραση.
- Προστέθηκαν οδηγίες για αυτοματοποιημένες εκδόσεις.

## V1.1.0 - 14 Ιουλίου 2018

Οι ακόλουθες αλλαγές αποτελούν μέρος της έκδοσης 1.1:

- Αφαιρέθηκε η Απαίτηση 2.6 "Το πρόχειρο είναι απενεργοποιημένο σε πεδία κειμένου που ενδέχεται να περιέχουν ευαίσθητα δεδομένα.".
- Προστέθηκε η Απαίτηση 2.2 "Δεν πρέπει να αποθηκεύονται ευαίσθητα δεδομένα εκτός του κοντέινερ της εφαρμογής ή των εγκαταστάσεων αποθήκευσης διαπιστευτηρίων συστήματος."
- Η απαίτηση 2.1 αναδιατυπώθηκε σε "Οι εγκαταστάσεις αποθήκευσης διαπιστευτηρίων συστήματος χρησιμοποιούνται κατάλληλα για την αποθήκευση ευαίσθητων δεδομένων, όπως PII, διαπιστευτήρια χρήστη ή κρυπτογραφικά κλειδιά.".

## V1.0 12 - Ιανουάριος 2018

Οι ακόλουθες αλλαγές αποτελούν μέρος της έκδοσης 1.0:

- Διεγράφη το 8.9 ως ταυτόσημο του 8.12
- Το 4.6 έγινε πιο γενικό
- Μικρές διορθώσεις (τυπογραφικά λάθη κλπ.)
