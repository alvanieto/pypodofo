%module pypodofo
%{
#include <base/PdfDefines.h>
#include <base/PdfString.h>
#include <base/PdfError.h>
#include <doc/PdfMemDocument.h>
#include <doc/PdfPage.h>
#include <doc/PdfField.h>

using namespace PoDoFo;
%}

#include <base/PdfDefines.h>
#include <base/PdfString.h>
#include <base/PdfError.h>
#include <doc/PdfMemDocument.h>
#include <doc/PdfPage.h>
#include <doc/PdfField.h>


typedef ptrdiff_t pdf_long;

enum EPdfField {
    ePdfField_PushButton,
    ePdfField_CheckBox,
    ePdfField_RadioButton,
    ePdfField_TextField,
    ePdfField_ComboBox,
    ePdfField_ListBox,
    ePdfField_Signature,

    ePdfField_Unknown = 0xff
};


class PdfError {
public:
    const char *what() const;
};


class PdfMemDocument {
public:
    PdfMemDocument(const char*);
    ~PdfMemDocument();

    int GetPageCount() const;
    PdfPage *GetPage(int) const;
    void Write(const char *);
};


class PdfPage {
public:
    PdfPage( PdfObject* pObject, const std::deque<PdfObject*> & listOfParents );
    int GetNumFields() const;
    const PdfField GetField(int) const;
    unsigned int GetPageNumber() const;
};

// Map PdfString as python string
%typemap(out) PdfString {
    $result = PyString_FromString($1.GetString());
}

// Map python string as PdfString
%typemap(typecheck, precedence=SWIG_TYPECHECK_POINTER) const PdfString & {
    $1 = PyString_Check($input) ? 1 : 0;
}

%typemap(in) const PdfString & (PdfString temp) {
    temp = PdfString(PyString_AsString($input));
    $1 = &temp;
}

class PdfField {
public:
    PdfField(const PdfField &);
    PdfString GetFieldName() const;
    PdfPage *GetPage() const;
    void SetFieldName(const PdfString&);
    EPdfField GetType() const;
};


class PdfTextField : public PdfField {
public:
    PdfTextField(const PdfField &);
    void SetText(const PdfString &) throw (PdfError);
    PdfString GetText() const;
    void SetMaxLen( pdf_long nMaxLen );
    pdf_long GetMaxLen() const;
};


class PdfListField : public PdfField {
public:
    PdfListField(const PdfField &);
    void InsertItem(const PdfString &rsValue, const PdfString &rsDisplayName=PdfString::StringNull);
    const PdfString GetItem(int) const;
    void RemoveItem(int);
    size_t GetItemCount() const;
    void SetSelectedItem(int);
    int GetSelectedItem() const;
};


class PdfComboBox : public PdfListField {
public:
    PdfComboBox(const PdfField &);
    void SetEditable(bool bEdit);
    bool IsEditable() const;
};


class PdfButton : public PdfField {
public:
    PdfButton(const PdfField &);
    bool IsPushButton() const;
    bool IsCheckBox() const;
    bool IsRadioButton() const;
    void SetCaption(const PdfString &rsText);
    const PdfString GetCaption() const;
};

class PdfPushButton : public PdfButton {
public:
    PdfPushButton(const PdfField &);
};


class PdfCheckBox : public PdfButton {
public:
    PdfCheckBox(const PdfField &);
    void SetChecked(bool bChecked);
    bool IsChecked() const;

};


class PdfString {
public:
    PdfString(const char *, const PdfEncoding * const pEncoding=NULL);
    const char* GetString() const;
};
