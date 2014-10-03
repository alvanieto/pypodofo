%module pypodofo
%{
#include <base/PdfString.h>
#include <doc/PdfMemDocument.h>
#include <doc/PdfPage.h>
#include <doc/PdfField.h>

using namespace PoDoFo;
%}

#include <base/PdfString.h>
#include <doc/PdfMemDocument.h>
#include <doc/PdfPage.h>
#include <doc/PdfField.h>

class PdfMemDocument {
public:
    int GetPageCount() const;
    PdfMemDocument(const char*);
    PdfPage *GetPage(int) const;
    void Write(const char *);
};


class PdfPage {
public:
    PdfPage( PdfObject* pObject, const std::deque<PdfObject*> & listOfParents );
    int GetNumFields() const;
    const PdfField GetField(int) const;
};

// Map PdfString as python string
%typemap(out) PdfString {
    $result = PyString_FromString($1.GetString());
}

class PdfField {
public:
    PdfField(const PdfField &);
    PdfString GetFieldName() const;
};


class PdfTextField {
public:
    PdfTextField(const PdfField &);
    void SetText(const PdfString &);
    void SetText(const char *);
};


class PdfString {
public:
    PdfString(const char *, const PdfEncoding * const pEncoding=NULL);
    const char* GetString() const;
};


void PdfTextField::SetText(const char *text)
{
    PdfField::SetText(PdfString(text));
}
